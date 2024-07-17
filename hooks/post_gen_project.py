#!/usr/bin/python3
import subprocess

try:
    subprocess.call(["curl", "-sSf", "https://rye.astral.sh/get", "|", "bash"])
    subprocess.call(["rye", "init"])
    subprocess.call(["rye", "add", "eth-ape", "--pre"])
    subprocess.call(["rye", "sync", "--pre"])
except Exception as e:
    print(f"An error occurred during initializing the git repo: {e}")
    print(
        "Makre sure to manually set up a git repository which is necessary for `hatch-vcs`"
    )