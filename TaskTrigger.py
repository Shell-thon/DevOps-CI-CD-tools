import re

with open(".env") as f:
    for line in f:
        if re.search("api|key|secret", line, re.I):
            print(f"⚠️ Possible secret: {line.strip()}")
