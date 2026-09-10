# ⚡ Universal Execution Kit: Fast-Track Ready (100-Engine Century Edition)

This document contains **all 100 pre-fetched Git Repos, terminal commands, configuration files, and copy-paste prompts** required to assemble the entire Master Execution Environment. You do not need to research anything—simply copy and paste the steps below in order.

---

## 🛠️ Step 0: Required Repository Registry (100 Engines)

Here is the complete registry of 100 open-source engines integrated into this setup:

```text
1. All-Hands-AI/OpenHands.git          2. affaan-m/ECC.git
3. geekan/MetaGPT.git                 4. crewAIInc/crewAI.git
5. microsoft/autogen.git               6. OpenBMB/ChatDev.git
7. princeton-nlp/SWE-agent.git        8. vanna-ai/vanna.git
9. argilla-io/argilla.git             10. great-expectations/great_expectations.git
11. guardrails-ai/guardrails.git      12. mit-ll-responsible-ai/hydra-zen.git
13. stanfordnlp/dspy.git              14. ShishirPatil/gorilla.git
15. guidance-ai/guidance.git          16. evalplus/evalplus.git
17. ray-project/ray.git               18. facebookresearch/hydra.git
19. bentoml/BentoML.git               20. tiangolo/fastapi.git
21. pola-rs/polars.git                22. triton-inference-server/server.git
23. pydantic/logfire.git              24. infiniflow/ragflow.git
25. THUDM/AutoGLM.git                 26. PrefectHQ/marvin.git
27. dair-ai/Prompt-Engineering-Guide  28. semgrep/semgrep.git
29. promptfoo/promptfoo.git           30. dottxt-ai/outlines.git
31. sqlfluff/sqlfluff.git             32. astral-sh/ruff.git
33. grafana/k6.git                    34. locustio/locust.git
35. astral-sh/uv.git                  36. pre-commit/pre-commit.git
37. duckdb/duckdb.git                 38. browser-use/browser-use.git
39. chroma-core/chroma.git            40. microsoft/graphrag.git
41. letta-ai/letta.git                42. paul-gauthier/aider.git
43. BerriAI/litellm.git               44. RooVetGit/Roo-Cline.git
45. assafelovic/gpt-researcher.git    46. stanford-oval/storm.git
47. run-llama/llama_index.git         48. langchain-ai/langchain.git
49. ollama/ollama.git                 50. vllm-project/vllm.git
51. SGLang-project/sglang.git         52. localstack/localstack.git
53. hasura/graphql-engine.git         54. dgraph-io/dgraph.git
55. temporalio/temporal.git           56. n8n-io/n8n.git
57. supabase/cli.git                  58. open-telemetry/opentelemetry-python.git
59. trpc/trpc.git                     60. prisma/prisma.git
61. meilisearch/meilisearch.git       62. redis/redis.git
63. nats-io/nats-server.git           64. minio/minio.git
65. traefik/traefik.git               66. hashicorp/vault.git
67. PostHog/posthog.git               68. getsentry/sentry.git
69. storybookjs/storybook.git         70. oven-sh/bun.git
71. shadcn-ui/ui.git                  72. biomejs/biome.git
73. tailwindlabs/tailwindcss.git      74. lucide-icons/lucide.git
75. framer/motion.git                 76. pmndrs/zustand.git
77. TanStack/query.git                78. nextauthjs/next-auth.git
79. stripe/stripe-node.git            80. resend/resend-node.git
81. astral-sh/rye.git                 82. vercel/turbo.git
83. vitejs/vite.git                   84. microsoft/playwright.git
85. cypress-io/cypress.git            86. mswjs/msw.git
87. colinhacks/zod.git                88. sinclairzx81/typebox.git
89. taskforcesh/bullmq.git            90. upstash/upstash-redis.git
91. drizzle-team/drizzle-orm.git      92. ClickHouse/ClickHouse.git
93. superfly/flyctl.git               94. pulumi/pulumi.git
95. opencost/opencost.git             96. aquasecurity/kube-bench.git
97. aquasecurity/trivy.git            98. bridgecrewio/checkov.git
99. typicode/husky.git                100. biomejs/biome.git
```

---

## 🚀 PHASE 1: Base Sandbox Launch (Copy-Paste)

### 📌 Command 1.1: Run Docker OpenHands Container (Windows PowerShell)
Open your PowerShell and run this exact command to start the secure Web Dashboard:

```powershell
docker run -it --rm `
    -e SANDBOX_USER_ID=0 `
    -e WORKSPACE_BASE="$PWD/workspace" `
    -v /var/run/docker.sock:/var/run/docker.sock `
    -v "$PWD/workspace:/opt/workspace" `
    -p 3000:3000 `
    --name openhands-app `
    docker.all-hands.dev/all-hands-ai/openhands:latest
```

*After running, open your browser and navigate to: `http://localhost:3000`*

---

## ⚙️ PHASE 2: Master Operating Instructions (`AGENTS.md`)

Copy and paste this master configuration into your project root as `./workspace/AGENTS.md`.

```markdown
# MASTER AGENT OPERATING INSTRUCTIONS (100-ENGINE CENTURY STACK)

## 1. Core Execution Philosophy
- Always PLAN before building (MetaGPT/CrewAI Mode).
- Execute strictly in the 5-Phase Streamlined Pipeline.
- Write Unit Tests BEFORE implementing feature code (ECC TDD Cycle).
- Maintain 100% Security & Syntax Awareness (Semgrep, Trivy, Outlines & Biome).

## 2. Planning Protocol (MetaGPT, CrewAI & AutoGen Mode)
Draft System Architecture, ERD, File Structure Tree & Sub-agent Assignments.

## 3. TDD Protocol (ECC & EvalPlus Mode)
Write failing tests in `tests/`, execute, write minimal code to pass, refactor with Ruff & Biome.

## 4. Virtual Review & Security Loop (ChatDev, SWE-agent & PromptFoo Mode)
Run SWE-agent security audits, SQLFluff database optimization, and Guardrails safety checks.

## 5. Free API Optimization (Groq & Gemini Flash via LiteLLM)
Route traffic dynamically: Groq Llama 3 for fast tasks, Gemini Flash for heavy context reasoning.
```

---

## 🔑 PHASE 3: Zero-Cost API Configuration (`config.toml`)

Copy and paste this configuration into `./workspace/config.toml`:

```toml
[llm]
model = "gemini/gemini-1.5-flash"
api_key = "YOUR_GEMINI_FREE_API_KEY"
embedding_model = "groq/llama-3-8b"
embedding_api_key = "YOUR_GROQ_FREE_API_KEY"
temperature = 0.2

[agent]
name = "CodeActAgent"
memory_enabled = true
max_iterations = 50

[sandbox]
timeout = 300
enable_auto_lint = true
```

---

## 🧪 PHASE 4: Master Execution Prompt (To Give the AI)

Whenever you want to build a complete production product, simply copy and paste this prompt into your OpenHands UI (`http://localhost:3000`):

```text
[TASK]: Build a Production-Grade Full-Stack Application.

[REQUIREMENTS]:
1. Read the AGENTS.md rules in the workspace.
2. Phase 1: Draft the PRD and File Architecture tree (MetaGPT & CrewAI flow).
3. Phase 2: Use TDD (Test-Driven Development) to write backend API endpoints and tests.
4. Phase 3: Implement UI frontend components using shadcn/ui and Tailwind CSS.
5. Phase 4: Run database tuning (SQLFluff), security checks (Semgrep/Trivy/Checkov) and execute E2E browser tests (Browser-Use/Playwright) to verify the app runs cleanly.

Start by creating the project structure and writing the initial test suite.
```

---
*Kit Version: 100.0 (Century Omni-Stack Loaded & Ready for Instant Deployment)*
