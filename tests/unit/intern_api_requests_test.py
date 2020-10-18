from unittest import TestCase, mock

from tasks.intern.api_requests.task import get_response


class TestAPIRequests(TestCase):
    @mock.patch("requests.get")
    def test_get_response(self, mock_requests):

        mock_requests.json.return_value = {"rates": {"CAD": 1.56, "HKD": 9.29}}
        mock_requests.response_code.return_value = 200

        self.assertTrue(get_response(), mock_requests.json.return_value)
