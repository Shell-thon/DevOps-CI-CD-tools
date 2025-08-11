import subprocess

print("🧹 Removing stopped containers...")
subprocess.call("docker container prune -f", shell=True)

print("🧼 Removing dangling images...")
subprocess.call("docker image prune -f", shell=True)
