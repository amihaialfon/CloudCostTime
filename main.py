# to run this file with pytest write "pytest test_security_events_api.py"
from api_client import SecurityEventsAPIClient
import requests

endpoint = "http://example.com/api"
valid_user_id = "valid_user_id"
invalid_user_id = "invalid_user_id"

if __name__ == "__main__":
    client = SecurityEventsAPIClient(endpoint)
    try:
        result = client.get_security_events(valid_user_id)
        print("API call successful:", result)
    except requests.exceptions.HTTPError as err:
        print("API call failed:", err)
