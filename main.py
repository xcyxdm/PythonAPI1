import os
import requests

def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("API_KEY is not set")

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    url = "https://api.github.com/user"
    response = requests.get(url, headers=headers, timeout=5)

    print("status:", response.status_code)
    print(response.json())

if __name__ == "__main__":
    main()