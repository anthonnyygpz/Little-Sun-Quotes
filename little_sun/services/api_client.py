import requests
from dataclasses import dataclass


@dataclass
class APIClient:
    # API Configuration
    BASE_URL = "http://0.0.0.0:8000"
    ENDPOINT = "/api/get_nail_services"

    def get_nail_services(self):
        try:
            full_url = f"{self.BASE_URL}{self.ENDPOINT}"
            response = requests.get(full_url)
            response.raise_for_status()

            print(response.json())
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching  information: {e}")
            return None
