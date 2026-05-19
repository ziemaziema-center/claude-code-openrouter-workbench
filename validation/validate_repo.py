from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "ARCHITECTURE.md",
    "QUICKSTART.md",
    "SECURITY.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "diagrams/pipeline.md",
]
SECRET_PATTERNS = [
    re.compile(r"sk-(?!or-REPLACE_ME)[A-Za-z0-9_\-]{16,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9\-]{16,}"),
    re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"),
    re.compile(r"(?i)(authorization:\s*bearer\s+)(?!REPLACE_ME)[A-Za-z0-9._\-]{16,}"),
    re.compile(r"(?i)(api[_-]?key|secret|token|access[_-]?key)\s*[:=]\s*(?!REPLACE_ME)(?!sk-or-REPLACE_ME)[A-Za-z0-9_\-]{12,}"),
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists():
        fail(f"missing {rel}")
    if path.suffix == ".md" and len(path.read_text(encoding="utf-8")) < 500:
        fail(f"{rel} needs more detail")

for folder in ["docs", "examples", "diagrams", "validation"]:
    if not (ROOT / folder).exists():
        fail(f"missing {folder}/")

all_text = []
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    all_text.append(text)
    for pattern in SECRET_PATTERNS:
        match = pattern.search(text)
        if match and "REPLACE_ME" not in match.group(0):
            fail(f"secret-like value in {path.relative_to(ROOT)}")

joined = "\n".join(all_text)
for phrase in ["validation-first", "memory-first", "safety", "telemetry"]:
    if phrase not in joined:
        fail(f"missing ecosystem term: {phrase}")

if "```mermaid" not in joined:
    fail("missing Mermaid diagram")

print("PASS: repo validation passed")
