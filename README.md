# Claude Code OpenRouter Workbench

A practical workbench for Claude Code with OpenRouter, DeepSeek, Ollama, and LiteLLM routing.

## What This Project Is

This repo documents safe local setup patterns for agent-assisted coding through Claude Code compatible environment variables and alternative model routing layers.

## Why It Exists

Developers want flexible model routing, but setup notes often mix real keys, shell-specific details, and unclear tradeoffs. This repo keeps setup reproducible and sanitized.

## Who It Helps

Developers using Claude Code, OpenRouter, DeepSeek, Ollama, LiteLLM, or local fallback models for coding workflows.

## Problem It Solves

It solves fragmented setup knowledge by comparing real Claude, OpenRouter, DeepSeek, and Ollama/LiteLLM paths in one public-safe workbench.

## Core Architecture

The workbench defines environment-variable profiles, routing comparison docs, troubleshooting, local-only workflows, and safety rules for key handling.

See [`ARCHITECTURE.md`](ARCHITECTURE.md) and [`diagrams/pipeline.md`](diagrams/pipeline.md) for the full system view.

## Safety Model

Only placeholders are included. The docs require local `.env` handling, shell history awareness, and no committed keys.

## Install and Setup

```bash
git clone https://github.com/ziemaziema-center/claude-code-openrouter-workbench.git
cd claude-code-openrouter-workbench
cp .env.example .env
```

Then keep fake values until you have reviewed [`SECURITY.md`](SECURITY.md) and the relevant quickstart.

## Example Usage

Copy `.env.example`, choose a provider profile in `docs/routing_comparison.md`, and keep all keys local.

## Production Ready vs Experimental

Production-ready:

- Documentation structure, safety model, and validation-first workflow.
- Sanitized examples and fixtures that are safe to publish.
- Issue and pull request templates for public collaboration.

Experimental:

- Any live connector, publisher, trading, or messaging integration.
- Any automation that depends on private credentials, private endpoints, or account-specific business rules.

## Screenshots and Diagrams

- Add screenshots under `docs/screenshots/` after public redaction.
- Start with the Mermaid diagrams in `diagrams/`.

## Roadmap

The first milestone is a fully reproducible local demo. Later milestones add optional integrations, richer fixtures, and community-maintained adapters.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), open an issue before large changes, and include validation evidence in every pull request.

## Disclaimer

Provider compatibility, pricing, and model availability change. Verify current provider docs before relying on a routing profile.

