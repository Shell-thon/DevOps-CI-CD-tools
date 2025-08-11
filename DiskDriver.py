import os

path = "."
for root, dirs, files in os.walk(path):
    total = sum(os.path.getsize(os.path.join(root, f)) for f in files)
    if total > 10 * 1024**2:  # >10MB
        print(f"{root}: {total // 1024**2} MB")
