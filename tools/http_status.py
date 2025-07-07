# tools/http_status.py
import sys
import requests
import time

def check_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        duration = time.time() - start
        print(f"\n✅ {url} responded with status {response.status_code} in {duration:.2f} seconds.")
    except requests.exceptions.Timeout:
        print(f"⏱️ Timeout: {url} took too long to respond.")
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection Error: Could not reach {url}.")
    except Exception as e:
        print(f"❌ Error checking {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python http_status.py <url>")
        sys.exit(1)
    check_url(sys.argv[1])
