import subprocess


def run_catc(cwd: str, path: str) -> str:
    return subprocess.check_output(
        f"catc {path}",
        shell=True,
        cwd=cwd,
    ).decode("utf-8")


def read(path: str) -> str:
    with open(path) as f:
        return f.read()
