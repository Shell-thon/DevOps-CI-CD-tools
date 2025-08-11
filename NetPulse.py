import subprocess

hosts = {
    "prod": "ubuntu@prod.example.com",
    "dev": "ubuntu@dev.example.com",
}

target = input("Connect to [prod/dev]: ")
if target in hosts:
    subprocess.call(f"ssh {hosts[target]}", shell=True)
