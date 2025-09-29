import os
import requests
import datetime

def main():
    zap_url = os.environ.get("ZAP_URL")
    if not zap_url:
        raise ValueError("ZAP_URL environment variable is not set")

    payload = {
        "source": "render-cron",
        "time": datetime.datetime.utcnow().isoformat() + "Z"
    }

    resp = requests.post(zap_url, json=payload, timeout=10)
    resp.raise_for_status()  # raise error if non-2xx

    print("Posted to Zapier:", resp.status_code)

if __name__ == "__main__":
    main()
