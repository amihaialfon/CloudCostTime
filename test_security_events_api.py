# to run this file with pytest write "pytest test_security_events_api.py" and enter

import pytest
from api_client import SecurityEventsAPIClient
from main import endpoint, valid_user_id, invalid_user_id


class TestSecurityEventsAPI:
    _failed = False

    @classmethod
    def setup_class(cls):
        cls.client = SecurityEventsAPIClient(endpoint)

    def test_valid_user_id(self, valid_user_id=valid_user_id):
        response = self.client.get_security_events(valid_user_id)
        assert response.status_code == 200
        assert 'customer_email' in response.json()
        assert 'number_of_events' in response.json()
        assert 'events' in response.json()

    def test_invalid_user_id(self, invalid_user_id=invalid_user_id):
        response = self.client.get_security_events(invalid_user_id)
        assert response.status_code == 404
        assert 'error' in response.json()

    def test_missing_user_id(self):
        response = self.client.get_security_events("")
        assert response.status_code == 400
        assert 'error' in response.json()
        assert 'missing_user_id' in response.json()['error']

    def test_invalid_user_format(self):
        response = self.client.get_security_events(123)
        assert response.status_code == 400
        assert 'error' in response.json()
        assert 'invalid_data_format' in response.json()['error']

    def test_large_user_id(self):
        user_id = "a" * 100
        response = self.client.get_security_events(user_id)
        assert response.status_code == 200
        assert 'customer_email' in response.json()

    @pytest.mark.parametrize("retry_count", [0, 1, 2])
    def test_retry_failed_test(self, retry_count):
        if retry_count > 0 and self._failed:
            pytest.skip("Retrying the failed test...")
        else:
            pytest.fail("The test has failed and cannot be retried.")

    def pytest_runtest_make_report(self, item, call):
        if call.excinfo is not None:
            self._failed = True
