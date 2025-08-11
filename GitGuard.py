import subprocess

status = subprocess.getoutput("git status --porcelain")
if status:
    print("⚠️ Repo is dirty! Uncommitted changes:")
    print(status)
else:
    print("✅ Repo is clean.")
