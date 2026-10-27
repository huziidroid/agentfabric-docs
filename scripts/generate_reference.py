"""Regenerate checked-in SDK field/signature references from a local source preview.

Run with Python 3.12+: python scripts/generate_reference.py /path/to/runtime
The website build uses the generated Markdown and needs no Runtime installation.
"""

import ast
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
RUNTIME = Path(sys.argv[1]).resolve()
SOURCE = RUNTIME / "src" / "agentfabric_runtime"
OUTPUT = PROJECT / "src/content/docs/reference/generated"
OUTPUT.mkdir(parents=True, exist_ok=True)
manifest = {}

GROUPS = {
    "core": ("Common values", [("core/schemas.py", None), ("core/identity.py", None)]),
    "artifacts": ("Artifact models and client", [("artifacts/schemas.py", None), ("artifacts/interfaces.py", None), ("services/artifact_service.py", {"ArtifactService"}), ("services/transactions.py", {"TransactionRetrySettings"})]),
    "permissions": ("Permission and admission models", [("permissions/schemas.py", None)]),
    "goals": ("Goal and task models", [("goals/schemas.py", {
        "AgentBinding", "TaskSpec", "GoalLimits", "GoalSpec", "TaskView", "GoalSnapshot", "GoalDetails", "GoalPage", "GoalEvent", "PausedGoalState"
    }), ("goals/invocations.py", {"TaskInvocation", "TaskContinuation"})]),
    "decisions": ("Decision, wait, and checkpoint models", [("goals/schemas.py", {
        "Checkpoint", "WaitSpec", "WaitResolution", "DecisionRequest", "CompletionCheckRequest", "CompletionReport", "AgentSignal", "DecisionReceipt", "GoalDecisionRecord", "DecisionState", "SignalEffect", "TaskResponse"
    })]),
    "outcomes": ("Task completion and outcome models", [("goals/schemas.py", {
        "TaskCompletion", "TaskCompletionV2", "TaskCompletionReceipt", "PendingExecutionOutcomeV1", "RecordedExecutionOutcomeV1", "RecordedExecutionOutcomeV2", "TaskOutcomeSnapshot"
    })]),
    "operations": ("Operation contracts", [("operations/schemas.py", None), ("operations/interfaces.py", None)]),
    "environment": ("Environment and execution contracts", [("environments/schemas.py", None), ("environments/client.py", None), ("execution/contracts.py", None)]),
    "scheduling": ("Scheduling development contracts", [("execution/schemas.py", None), ("execution/scheduling_schemas.py", None), ("execution/interfaces.py", None), ("environments/interface.py", None)]),
    "clients": ("Native client method signatures", [
        ("runtime.py", {"Runtime", "SQLiteRuntimeSettings"}),
        ("storage/repositories/credential_repo.py", {"SQLCredentialStore"}),
        ("permissions/interfaces.py", None),
        ("storage/provider_credentials.py", {"FileCredentialSource"}),
        ("services/goals.py", {"SQLGoalClient"}),
        ("goals/interfaces.py", {"TaskCompletionClient", "TaskHandler", "AssessmentHandler", "CompletionCheckHandler"}),
        ("services/task_coordinator.py", {"TaskCoordinator"}),
    ]),
}


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ").replace("`", "&#96;")


def fields(node, classes, seen=None):
    seen = set() if seen is None else seen
    if node.name in seen:
        return {}
    seen.add(node.name)
    result = {}
    for base in node.bases:
        if isinstance(base, ast.Name) and base.id in classes:
            result.update(fields(classes[base.id], classes, seen))
    for entry in node.body:
        if isinstance(entry, ast.AnnAssign) and isinstance(entry.target, ast.Name):
            if not entry.target.id.startswith("_") and entry.target.id != "model_config":
                result[entry.target.id] = (ast.unparse(entry.annotation), ast.unparse(entry.value) if entry.value else "Required")
    return result


for slug, (title, modules) in GROUPS.items():
    lines = ["---", f"title: {title}", f"description: Source-derived fields and signatures for the unreleased SDK preview.", "---", "", "> **Unreleased source preview.** Generated declarations describe types, not a promise that every contract has an executable implementation. Read the [behavioral API reference](../../overview/) and [capability matrix](../../../runtime/capabilities/) first.", "", "Field defaults shown as `Field(...)` include validation metadata. A `Field(...)` without `default=` or `default_factory=` is required. Inherited fields from classes in the same source module are included. Cross-field invariants are explained in the concept and behavioral reference pages.", ""]
    if slug in {"environment", "scheduling", "operations"}:
        lines += [":::caution[Extension contracts]", "These declarations include future facades and experimental scheduling interfaces. They are not additional attributes on `Runtime` and do not qualify physical execution, isolation, or termination.", ":::", ""]
    for relative, selected in modules:
        path = SOURCE / relative
        data = path.read_bytes()
        manifest[relative] = hashlib.sha256(data).hexdigest()
        tree = ast.parse(data.decode())
        module = "agentfabric_runtime." + relative.removesuffix(".py").replace("/", ".")
        classes = {n.name: n for n in tree.body if isinstance(n, ast.ClassDef)}
        lines += [f"## `{module}`", ""]
        # Include public type aliases/limits, keeping implementation configuration private.
        if relative.endswith("schemas.py") and slug not in {"decisions", "outcomes", "goals"}:
            for node in tree.body:
                if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                    name = node.targets[0].id
                    if name.startswith("_") or name in {"VALIDATION_CONFIG"}:
                        continue
                    lines += [f"### `{name}`", "", "```python", ast.unparse(node), "```", ""]
        for name, node in classes.items():
            if name.startswith("_") or (selected is not None and name not in selected):
                continue
            lines += [f"### `{name}`", "", f"Import: `{module}.{name}`", ""]
            doc = ast.get_docstring(node)
            if doc:
                lines += [doc, ""]
            values = fields(node, classes)
            if values:
                lines += ["| Field | Type | Default / validation |", "| --- | --- | --- |"]
                for field, (annotation, default) in values.items():
                    lines += [f"| `{field}` | `{cell(annotation)}` | `{cell(default)}` |"]
                lines += [""]
            is_protocol = any("Protocol" in ast.unparse(base) for base in node.bases)
            if slug == "clients" or is_protocol or name in {"EnvironmentReadiness", "ArtifactService"}:
                for method in node.body:
                    if not isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)) or (method.name.startswith("_") and not (method.name == "__init__" and name in {"FileCredentialSource", "ArtifactService"})):
                        continue
                    if method.name.startswith("validate_"):
                        continue
                    signature = copy.deepcopy(method)
                    signature.decorator_list = []
                    signature.body = [ast.Expr(value=ast.Constant(value=Ellipsis))]
                    lines += [f"#### `{name}.{method.name}`", "", "```python", ast.unparse(signature), "```", ""]
                    if ast.get_docstring(method):
                        lines += [ast.get_docstring(method), ""]
    (OUTPUT / f"{slug}.md").write_text("\n".join(lines))

head = subprocess.check_output(["git", "-C", str(RUNTIME), "rev-parse", "HEAD"], text=True).strip()
(PROJECT / "sdk-reference-baseline.json").write_text(json.dumps({
    "status": "unreleased working-tree preview; HEAD alone does not reproduce these APIs",
    "recorded_date": "2026-10-27", "parent_commit": head, "source_sha256": manifest,
}, indent=2) + "\n")
print(f"Generated {len(GROUPS)} reference pages from {len(manifest)} source modules.")
