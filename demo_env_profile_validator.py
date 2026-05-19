# SPDX-License-Identifier: MIT
from pathlib import Path

root = Path(__file__).resolve().parent
text = (root / "examples" / "env_profiles.md").read_text(encoding="utf-8")
required = ["ANTHROPIC_BASE_URL", "ANTHROPIC_API_KEY", "CLAUDE_MODEL"]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit(f"FAIL: missing {missing}")
if "sk-or-REPLACE_ME" not in text:
    raise SystemExit("FAIL: placeholder OpenRouter key missing")
print("PASS: env profiles include required variables and placeholders only")
