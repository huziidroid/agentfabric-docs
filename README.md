# AgentFabric documentation

Public documentation built with Astro Starlight and hosted on GitHub Pages. This project is separate from Runtime's internal development documents.

## Local development

Use Node.js 24.13.0 or newer (Node 24 LTS recommended) and pnpm 10.11.0.

```sh
nvm use
pnpm install --frozen-lockfile
pnpm dev
```

Open the printed URL including `/agentfabric-docs/`. Search is indexed during production builds; verify it with the production preview.

```sh
pnpm validate
pnpm preview
```

## Authoring

Pages live in `src/content/docs/`. Add Markdown or MDX with `title` and `description` frontmatter, then add navigation entries in `astro.config.mjs`. Styling lives in `src/styles/custom.css`.

Use relative page links with trailing slashes so links work under the Pages subpath. Describe supported behavior and label planned capabilities explicitly. Do not publish internal review logs, credentials, local paths, or implementation history.

## GitHub Pages

- Repository: https://github.com/huziidroid/agentfabric-docs
- Publishing branch: `master`
- Configured address: https://huziidroid.github.io/agentfabric-docs/

1. Open **Settings → Pages** in the repository.
2. Set **Build and deployment → Source** to **GitHub Actions**.
3. Push to `master`, or run **Deploy documentation** in Actions.

The deploy workflow checks, builds, uploads, and publishes. Pull requests check and build without deploying. No third-party hosting account or deployment token is required.

To change repository owner or name, update `site`, `base`, the social link, and `editLink` in `astro.config.mjs`. For a custom domain, update `site`, set `base` to `/`, add `public/CNAME`, and configure DNS and GitHub Pages.

## References

- [Starlight](https://starlight.astro.build/)
- [Astro GitHub Pages deployment](https://docs.astro.build/en/guides/deploy/github/)

## Documentation quality and source reference

The site follows the tutorial / guide / concept / reference structure in [DOCUMENTATION_SPEC.md](DOCUMENTATION_SPEC.md). The public capability matrix links each implemented SDK family to its explanation, guide, and reference. Unreleased and contract-only behavior is labeled explicitly.

`pnpm validate` runs Astro diagnostics, a production build, and internal route/anchor/asset plus search-asset checks. CI runs the same command. The complete Python examples are embedded directly from `examples/`, so tutorial code and executable source stay together.

With Python 3.12+ and a compatible Runtime checkout, refresh source-derived references using:

```sh
python scripts/generate_reference.py /path/to/agentfabric-runtime
python examples/native_runtime.py
python examples/declare_goal.py
```

The example commands require that compatible SDK to be installed in the active Python environment. `sdk-reference-baseline.json` records the parent commit and exact source-file hashes; parent HEAD alone may not include this unreleased API. Review generated diffs and behavioral pages together. Website builds require no Python or local SDK.
