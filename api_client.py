# to run this file with pytest write "pytest test_security_events_api.py" and enter
import requests
from retrying import retry

class SecurityEventsAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def get_security_events(self, user_id):
        endpoint = f"{self.base_url}/security-events/{user_id}"
        response = requests.get(endpoint)
        return response
