from fake_headers import Headers
import requests

from modules.errors_handling import DaimngError


class APOD_api():
    def __init__(self, key):
        self._url = 'https://api.nasa.gov/planetary/apod'
        self._params = {
            'api_key': key
            }
        self.headers = Headers(
            browser="firefox",
            os="mac",
        ).generate()
        
    def get_apod(self) -> dict:
        response_raw = self._make_request()
        return response_raw.json()
    
    def test_connection(self) -> bool:
        response_raw = self._make_request()
        response = response_raw.json()
        
        if response.get('error'):
            if response.get('error').get('code') == 'API_KEY_INVALID':
                return False
        return True
    
    def _make_request(self) -> requests.Response:
        response = requests.get(
            self._url,
            params=self._params,
            headers=self.headers
        )
        respones_code = response.status_code
        if respones_code not in range(200, 300):
            raise DaimngError(str(respones_code), 'NASA_APOD')

        return response