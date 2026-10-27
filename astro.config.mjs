import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://huziidroid.github.io',
  base: '/agentfabric-docs',
  trailingSlash: 'always',
  integrations: [
    starlight({
      title: 'AgentFabric',
      description: 'Public documentation for the AgentFabric Runtime SDK preview.',
      favicon: '/favicon.svg',
      social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/huziidroid/agentfabric-docs' }],
      editLink: { baseUrl: 'https://github.com/huziidroid/agentfabric-docs/edit/master/' },
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        {
                "label": "Start here",
                "items": [
                        {
                                "label": "Introduction",
                                "slug": "getting-started/introduction"
                        },
                        {
                                "label": "Runtime at a glance",
                                "slug": "getting-started/runtime-overview"
                        },
                        {
                                "label": "Installation",
                                "slug": "getting-started/installation"
                        },
                        {
                                "label": "First artifact",
                                "slug": "tutorials/native-runtime"
                        },
                        {
                                "label": "First goal",
                                "slug": "tutorials/declare-goal"
                        }
                ]
        },
        {
                "label": "Concepts",
                "items": [
                        {
                                "label": "Core values",
                                "slug": "runtime/concepts"
                        },
                        {
                                "label": "Identities and credentials",
                                "slug": "runtime/identities"
                        },
                        {
                                "label": "Permissions and inheritance",
                                "slug": "runtime/permissions"
                        },
                        {
                                "label": "Connections and secrets",
                                "slug": "runtime/connections"
                        },
                        {
                                "label": "Admission and effect safety",
                                "slug": "runtime/admission"
                        },
                        {
                                "label": "Artifacts and storage",
                                "slug": "runtime/artifacts"
                        },
                        {
                                "label": "Goals, tasks, and executions",
                                "slug": "runtime/lifecycle"
                        },
                        {
                                "label": "Decisions and controls",
                                "slug": "runtime/decisions"
                        },
                        {
                                "label": "Waits",
                                "slug": "runtime/waits"
                        },
                        {
                                "label": "Checkpoints and Resume",
                                "slug": "runtime/checkpoints"
                        },
                        {
                                "label": "Before-start Retry",
                                "slug": "runtime/retry"
                        },
                        {
                                "label": "Returns and outcomes",
                                "slug": "runtime/outcomes"
                        },
                        {
                                "label": "Durability and budgets",
                                "slug": "runtime/durability"
                        },
                        {
                                "label": "Extension boundaries",
                                "slug": "runtime/extensions"
                        }
                ]
        },
        {
                "label": "Task guides",
                "items": [
                        {
                                "label": "Open and close Runtime",
                                "slug": "guides/runtime-lifecycle"
                        },
                        {
                                "label": "Bootstrap and rotate credentials",
                                "slug": "guides/credentials"
                        },
                        {
                                "label": "Manage artifacts",
                                "slug": "guides/artifacts"
                        },
                        {
                                "label": "Issue grants and bind access",
                                "slug": "guides/permissions"
                        },
                        {
                                "label": "Manage connections",
                                "slug": "guides/connections"
                        },
                        {
                                "label": "Admit an external action",
                                "slug": "guides/admission"
                        },
                        {
                                "label": "Declare and inspect a goal",
                                "slug": "guides/goals"
                        },
                        {
                                "label": "Apply decisions and controls",
                                "slug": "guides/decisions"
                        },
                        {
                                "label": "Resolve waits",
                                "slug": "guides/waits"
                        },
                        {
                                "label": "Continue or retry",
                                "slug": "guides/recovery"
                        },
                        {
                                "label": "Record and reconcile returns",
                                "slug": "guides/outcomes"
                        }
                ],
                "collapsed": true
        },
        {
                "label": "API reference",
                "items": [
                        {
                                "label": "Service map and conventions",
                                "slug": "reference/overview"
                        },
                        {
                                "label": "Runtime and settings",
                                "slug": "reference/runtime"
                        },
                        {
                                "label": "Identity administration",
                                "slug": "reference/identity"
                        },
                        {
                                "label": "Artifacts",
                                "slug": "reference/artifacts"
                        },
                        {
                                "label": "Permissions",
                                "slug": "reference/permissions"
                        },
                        {
                                "label": "Connections and credentials",
                                "slug": "reference/connections"
                        },
                        {
                                "label": "Authority and admission",
                                "slug": "reference/authority"
                        },
                        {
                                "label": "Goals and decisions",
                                "slug": "reference/goals"
                        },
                        {
                                "label": "Completions and coordinator",
                                "slug": "reference/completions"
                        },
                        {
                                "label": "Errors and limits",
                                "slug": "reference/errors"
                        },
                        {
                                "label": "Exact schemas and signatures",
                                "collapsed": true,
                                "items": [{ "autogenerate": { "directory": "reference/generated" } }]
                        }
                ],
                "collapsed": true
        },
        {
                "label": "Support",
                "items": [
                        {
                                "label": "Current capabilities",
                                "slug": "runtime/capabilities"
                        },
                        {
                                "label": "Compatibility and baseline",
                                "slug": "support/compatibility"
                        },
                        {
                                "label": "Troubleshooting",
                                "slug": "support/troubleshooting"
                        },
                        {
                                "label": "Glossary",
                                "slug": "support/glossary"
                        }
                ]
        }
],
    }),
  ],
});
