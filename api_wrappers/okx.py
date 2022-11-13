import hashlib
import hmac
import os
import typing as t

import requests
from logger.logger_conf import get_logger
from utilities.time import get_timestamp


class OkxClientBase:
    """
    Credentials to OKX API `trade_bot`
    """

    _rest_domain = 'https://www.okx.com'

    logger = get_logger()

    def __init__(self, *arsgs, **kwargs):
        self.__access_key = os.environ['API_KEY']
        self.__api_passphrase = os.environ['API_PASSPHRASE']
        self.__api_secret = os.environ['API_SECRET_KEY']

    def __get_signature(self, timestamp: str, method: str, request_path: str):
        creds = f'{timestamp}{method}{request_path}'
        return hmac.new(bytes(self.__api_secret, 'utf8'), msg=bytes(creds, 'utf8'), digestmod='sha256').hexdigest().upper()

    def _get_private_request_headers(self, method: str, request_path: str):
        timestamp = get_timestamp()
        return {
            'OK-ACCESS-KEY': self.__access_key,   # The APIKey as a String.
            'OK-ACCESS-SIGN': self.__get_signature(timestamp, method, request_path),    # SHA256 signature
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-PASSPHRASE': self.__api_passphrase,
        }

    @classmethod
    def test_preview(cls) -> bool:
        instance = cls()
        headers = instance._get_private_request_headers('GET', '/tst/')
        import json
        print(
            json.dumps(headers, indent=4)
        )
        return True

    def execute_request(self, url, method, authorization: bool, body: t.Any = {}, headers: t.Dict[str, str] = {}):
        request_params = {
            'method': method,
            'url': f'{self._rest_domain}{url}',
        }
        if authorization:
            request_params['headers'] = headers.update(self._get_private_request_headers(method, url))
        request_params['headers'] = headers
        try:
            response = requests.request(**request_params)
        except Exception as e:
            self.logger.exception('error')
            return
        return response


class OkxClient(OkxClientBase):
    """
    Use this class when make request to OKX.
    """

    def get_account_balance(self):
        url = '/api/v5/account/balance'
        method = 'GET'
        resp = self.execute_request(url, method, authorization=True)
        return resp

