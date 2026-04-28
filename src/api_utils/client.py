import requests

def get_json(url: str, headers: dict = None, timeout: int = 10):
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def post_json(url: str, data: dict, headers: dict = None, timeout: int = 10):
    try:
        response = requests.post(url, json=data, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None
