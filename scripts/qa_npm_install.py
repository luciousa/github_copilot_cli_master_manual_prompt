"""Test a version-pinned npm lifecycle in a disposable Windows prefix."""
import os
from pathlib import Path
import subprocess
import tempfile

root = Path(tempfile.mkdtemp(prefix="copilot-npm-reference-"))
prefix = root / "prefix"
prefix.mkdir()
userconfig = root / "npmrc"
userconfig.write_text("", encoding="utf-8")
env = os.environ.copy()
for key in list(env):
    if key.upper() in ("GH_TOKEN", "GITHUB_TOKEN", "COPILOT_GITHUB_TOKEN", "GITHUB_COPILOT_TOKEN") or key.lower().startswith("npm_config_"):
        env.pop(key, None)
env.update(NPM_CONFIG_USERCONFIG=str(userconfig), NPM_CONFIG_CACHE=str(root / "npm-cache"),
           COPILOT_HOME=str(root / "copilot-home"), COPILOT_CACHE_HOME=str(root / "copilot-cache"),
           COPILOT_AUTO_UPDATE="false")
npm = Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "nodejs" / "npm.cmd"
records = ["Windows npm lifecycle; disposable prefix, cache and Copilot home; "
           "npm user config isolated, auth environment removed. Version pinned to 1.0.109."]


def run(label, arguments, timeout=150):
    try:
        p = subprocess.run(arguments, env=env, cwd=root, stdin=subprocess.DEVNULL,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           text=True, encoding="utf-8", errors="replace", timeout=timeout)
        lines = p.stdout.replace(str(root), "<TEMP>").splitlines()
        records.append(f"## {label}\nExit: {p.returncode}\n" + "\n".join(lines[-8:]))
        print(f"{label}: exit {p.returncode}", flush=True)
        return p.returncode
    except subprocess.TimeoutExpired:
        records.append(f"## {label}\nTimed out after {timeout} seconds")
        print(f"{label}: timed out", flush=True)
        return None


install = run("npm install", [str(npm), "install", "-g", "--prefix", str(prefix),
                               "--registry=https://registry.npmjs.org", "@github/copilot@1.0.109"])
binary = prefix / "copilot.cmd"
records.append(f"Expected npm shim present after install: {binary.exists()}")
if install == 0 and binary.exists():
    run("installed CLI version", [str(binary), "--no-auto-update", "--version"], timeout=45)
    run("npm uninstall", [str(npm), "uninstall", "-g", "--prefix", str(prefix), "@github/copilot"])
    records.append(f"Expected npm shim absent after uninstall: {not binary.exists()}")
Path("research/evidence/copilot-1.0.109-npm-fixture.txt").write_text("\n\n".join(records) + "\n", encoding="utf-8")
print("Evidence saved.", flush=True)
