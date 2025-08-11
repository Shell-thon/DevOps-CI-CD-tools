import re
import time

log_file = "your.log"
pattern = re.compile("ERROR|WARN")

with open(log_file, "r") as f:
    f.seek(0, 2)  # go to end
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.5)
            continue
        if pattern.search(line):
            print(f"\033[91m{line.strip()}\033[0m")  # red highlight
