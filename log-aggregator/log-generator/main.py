import requests
import random
import time

ENDPOINT = "http://<INGRESS-IP>/logs"

levels = ["INFO", "DEBUG", "WARN", "ERROR"]
sources = ["frontend", "parser", "auth", "api"]

while True:
    log = {
        "level": random.choice(levels),
        "message": f"Log message {random.randint(1000, 9999)}",
        "source": random.choice(sources)
    }
    try:
        r = requests.post(ENDPOINT, json=log)
        print(f"{r.status_code}: {log}")
    except Exception as e:
        print("Error:", e)
    time.sleep(2)
