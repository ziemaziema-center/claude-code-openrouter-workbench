# Architecture

## System Intent

Provide practical model routing guidance without bundling secrets or implying that every provider has identical behavior.

## Main Components

- Environment variable profiles.
- Provider comparison matrix.
- Troubleshooting guide.
- Safe local workflow.
- Prompt and agent role examples.
- Redaction checklist.

## Data Flow

A developer selects a routing profile, sets local environment variables, runs Claude Code or compatible tooling, and records provider-specific limitations.

## Trust Boundaries

- Local operator workspace.
- Sanitized public fixtures.
- Optional external APIs, which are disabled or stubbed in public examples.
- Telemetry and logs, which must never contain secrets.

## Failure Handling

- Prefer fail-closed behavior.
- Preserve append-only audit context for decisions.
- Use validation before mutation.
- Escalate ambiguous states to human review.

## Extension Points

- Add new provider profiles.
- Add benchmark tasks.
- Add LiteLLM config examples.
- Add local Ollama model recipes.
- Add failure telemetry templates.

