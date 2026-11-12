"""Probe Copilot authentication with a harmless prompt in a disposable directory."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

root = Path(tempfile.mkdtemp(prefix="copilot-reference-auth-probe-"))
work = root / "workspace"
work.mkdir()
env = os.environ.copy()
env["COPILOT_HOME"] = str(root / "copilot-home")
env["COPILOT_CACHE_HOME"] = str(root / "copilot-cache")
env["COPILOT_AUTO_UPDATE"] = "false"
for key in ("GH_TOKEN", "GITHUB_TOKEN", "COPILOT_GITHUB_TOKEN", "GITHUB_COPILOT_TOKEN"):
    env.pop(key, None)
cli = shutil.which("copilot")
if not cli:
    raise SystemExit("Copilot executable not found")
args = [cli, "--no-auto-update", "--trust-folder", "-p",
        "Reply with exactly READY. Do not use tools or access any files."]
try:
    result = subprocess.run(args, cwd=work, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True, encoding="utf-8",
                            errors="replace", timeout=60)
    output = result.stdout.replace(str(root), "<TEMP>")
    # Capture only the test outcome, not raw session output or credentials.
    ready = any(line.strip() == "READY" for line in output.splitlines())
    message = ("Windows; disposable empty workspace and COPILOT_HOME; token "
               "environment variables removed; auto-update disabled.\n"
               f"Exit code: {result.returncode}\nExact READY line observed: {ready}\n")
except subprocess.TimeoutExpired:
    message = "Windows; disposable empty workspace; probe timed out after 60 seconds.\n"
Path("research/evidence/copilot-authenticated-probe.txt").write_text(message, encoding="utf-8")
print(message, end="")
