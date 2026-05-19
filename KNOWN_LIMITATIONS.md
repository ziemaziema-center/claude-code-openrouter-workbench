# Known Limitations

        Claude Code OpenRouter Workbench is intentionally conservative. Public trust matters more than pretending the project is a complete hosted product.

        ## Current Limits

        - Provider compatibility and model names change over time.
- This repo does not ship real API keys or billing guidance.
- Local model quality depends heavily on hardware and model choice.

        ## Architecture Tradeoffs

        - Fixture-first onboarding is safer than live demos, but less visually exciting.
        - Markdown-first structure works across agent tools, but does not enforce behavior unless teams run validation.
        - Approval gates slow down automation, but they make publishing, messaging, and finance workflows reviewable.

        ## Known Issues

        - Anthropic-compatible environment variables do not guarantee identical provider behavior.
- Some routers transform requests or tool behavior in provider-specific ways.

        ## Future Work

        - Provider smoke-test fixtures.
- PowerShell, Bash, and Fish setup variants.
- Compatibility matrix maintained by issues.

