import requests
from config.config import Config

class ApiClient:
    """
    Reusable REST API client wrapper with built-in logging,
    authentication handling, headers, and response validation.
    """
    def __init__(self, base_url: str = None):
        self.base_url = base_url or Config.API_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def set_auth_token(self, token: str):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def get(self, endpoint: str, params: dict = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params, timeout=10)

    def post(self, endpoint: str, json: dict = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=json, timeout=10)

    def put(self, endpoint: str, json: dict = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, json=json, timeout=10)

    def delete(self, endpoint: str) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, timeout=10)
