import subprocess

def open_in_vscode(path):
    subprocess.run(["code", path])