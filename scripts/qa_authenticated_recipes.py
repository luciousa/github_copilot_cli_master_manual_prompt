"""Exercise selected read-only recipe prompts against a synthetic repository."""
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

root = Path(tempfile.mkdtemp(prefix="copilot-reference-fixtures-"))
work = root / "workspace"
work.mkdir()
(work / "README.md").write_text("# Fixture shop\nNode order service and React client.\n", encoding="utf-8")
(work / "api.js").write_text(
    "// Synthetic fixture only\nfunction page(items, offset, size) {\n"
    "  return items.slice(offset, offset + size - 1);\n}\nmodule.exports = { page };\n",
    encoding="utf-8",
)
(work / "api.test.js").write_text(
    "// Expected: page([1, 2, 3], 0, 2) returns [1, 2].\n", encoding="utf-8"
)
(work / "ui.jsx").write_text("// Synthetic React consumer of order pages.\n", encoding="utf-8")
env = os.environ.copy()
env["COPILOT_HOME"] = str(root / "copilot-home")
env["COPILOT_CACHE_HOME"] = str(root / "copilot-cache")
env["COPILOT_AUTO_UPDATE"] = "false"
for key in ("GH_TOKEN", "GITHUB_TOKEN", "COPILOT_GITHUB_TOKEN", "GITHUB_COPILOT_TOKEN"):
    env.pop(key, None)
cli = shutil.which("copilot")
if not cli:
    raise SystemExit("Copilot executable not found")

cases = [
    ("K01", "Map this synthetic repository. Name relevant files and their roles. "
     "Cite evidence. Do not modify files or run shell commands."),
    ("K04", "Convert this synthetic feature brief into acceptance criteria: "
     "show a paginated order list only to the signed-in owner. Include normal, "
     "empty and unauthorized cases. Do not modify files or run shell commands."),
    ("K16", "Inspect api.js and api.test.js. Explain the pagination regression "
     "and a minimal failing input with expected and actual results. "
     "Do not modify files or run shell commands."),
    ("K21", "Inspect api.js and api.test.js. Propose a regression test for the "
     "pagination boundary that fails before correction. Explain the assertion. "
     "Do not modify files or run shell commands."),
]

def hashes():
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in work.iterdir() if p.is_file()}

log = ["Windows; synthetic fixture only; disposable Copilot home; environment token "
       "variables removed; automatic update disabled. Prompts requested read-only work. "
       "Output is model-generated and has not been independently accepted.\n"]
version = subprocess.run([cli, "--no-auto-update", "--version"], cwd=work, env=env,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, encoding="utf-8", errors="replace", timeout=30)
log.append("Version output: " + version.stdout.strip().replace(str(root), "<TEMP>") + "\n")
for name, prompt in cases:
    before = hashes()
    args = [cli, "--no-auto-update", "--trust-folder", "--silent", "-p", prompt]
    try:
        result = subprocess.run(args, cwd=work, env=env, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True, encoding="utf-8",
                                errors="replace", timeout=60)
        text = result.stdout.replace(str(root), "<TEMP>")
        log.append(f"## {name}\nExit: {result.returncode}\nTop-level regular files unchanged: {before == hashes()}\n"
                   f"Prompt: {prompt}\nOutput:\n{text}\n")
        print(f"{name}: exit {result.returncode}; top-level regular files unchanged: {before == hashes()}", flush=True)
    except subprocess.TimeoutExpired:
        log.append(f"## {name}\nTimed out after 60 seconds\nTop-level regular files unchanged: {before == hashes()}\n")
        print(f"{name}: timed out", flush=True)
    Path("research/evidence/copilot-recipe-fixtures.txt").write_text("\n".join(log), encoding="utf-8")
