import unittest
from unittest.mock import patch, MagicMock
from main import get_coindesk_data


class TestGetCoindeskData(unittest.TestCase):

    @patch('requests.get')
    def test_get_coindesk_data(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'key': 'value'}

        mock_requests_get.return_value = mock_response

        result = get_coindesk_data()

        mock_requests_get.assert_called_once_with("https://api.coindesk.com/v1/bpi/currentprice.json")
        mock_response.json.assert_called_once_with()
        self.assertEqual(result, {'key': 'value'})
