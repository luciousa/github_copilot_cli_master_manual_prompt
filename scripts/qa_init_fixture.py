"""Test `copilot init` in a synthetic repository without user project files."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

root = Path(tempfile.mkdtemp(prefix="copilot-reference-init-"))
repo = root / "repo"
repo.mkdir()
(repo / "README.md").write_text("# Synthetic calculator\nAdd two integers.\n", encoding="utf-8")
(repo / "calc.py").write_text("def add(a, b):\n    return a + b\n", encoding="utf-8")
env = os.environ.copy()
env.update(COPILOT_HOME=str(root / "copilot-home"),
           COPILOT_CACHE_HOME=str(root / "copilot-cache"), COPILOT_AUTO_UPDATE="false")
for key in ("GH_TOKEN", "GITHUB_TOKEN", "COPILOT_GITHUB_TOKEN", "GITHUB_COPILOT_TOKEN"):
    env.pop(key, None)
subprocess.run(["git", "init", "--quiet"], cwd=repo, env=env, check=True)
cli = shutil.which("copilot")
args = [cli, "--no-auto-update", "init"]
summary = ["Windows CLI 1.0.109; disposable synthetic Git repository and Copilot "
           "home; token environment variables removed; non-interactive stdin; "
           "automatic update disabled. Only synthetic files were supplied."]
try:
    result = subprocess.run(args, cwd=repo, env=env, stdin=subprocess.DEVNULL,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, encoding="utf-8", errors="replace", timeout=75)
    summary.append(f"Exit code: {result.returncode}")
    target = repo / ".github" / "copilot-instructions.md"
    summary.append(f"Instruction file created: {target.exists()}")
    if target.exists():
        summary.append("Generated file (synthetic content, not verified guidance):\n" + target.read_text(encoding="utf-8", errors="replace"))
    # Record the outcome only; avoid copying raw logs or credentials.
except subprocess.TimeoutExpired:
    summary.append("Timed out after 75 seconds; outcome is inconclusive.")
    summary.append(f"Instruction file present at timeout: {(repo / '.github' / 'copilot-instructions.md').exists()}")
evidence = "\n\n".join(summary) + "\n"
Path("research/evidence/copilot-1.0.109-init-fixture.txt").write_text(evidence, encoding="utf-8")
print("\n".join(summary[:3]), flush=True)
