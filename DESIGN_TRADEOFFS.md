# Design Tradeoffs

## Why This Shape

This exists because model routing setup is usually learned from scattered snippets, and those snippets often omit the caveats that matter when tools behave differently.

## Decisions That Were Intentional

- Prefer plain files over hidden state so a reviewer can inspect the operating model.
- Prefer fixture paths before live integrations so a new contributor can reproduce behavior safely.
- Prefer explicit human approval for risky actions over pretending automation can infer intent.

## What Was Intentionally Avoided

Pretending every Anthropic-compatible route behaves the same. The docs keep provider tradeoffs visible instead of hiding them behind one generic setup.

## Why Simpler Alternatives Were Not Enough

A README-only approach explains intent but does not create a repeatable operating loop. A script-only approach can validate structure but cannot capture judgment. The current shape keeps docs, examples, and validation close together because the failure modes usually happen between those layers.

## What Still Feels Messy

Model IDs change. Routers transform requests. Tool use differs. Local models vary by hardware. Error messages often point to the wrong layer.

## Where the Architecture May Break

The workflow breaks when a user copies environment variables into a repo, assumes provider parity, or debugs a model issue as if it were a tool issue.

## Scalability Concerns

The first scaling problem is not traffic. It is consistency. As more examples and adapters are added, each one must preserve the same safety boundary, fixture discipline, and validation expectation. Without that, the repo becomes a pile of special cases.

## Human Approval Still Required

Humans still choose provider risk, cost, privacy tradeoffs, and whether a model's output quality is acceptable for a task.

