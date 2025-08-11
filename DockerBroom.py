import requests
import time

url = "https://example.com"
for i in range(3):
    try:
        r = requests.get(url, timeout=5)
        print(f"{url} is UP: {r.status_code}")
        break
    except:
        print(f"Attempt {i+1}: {url} is DOWN")
        time.sleep(3)
