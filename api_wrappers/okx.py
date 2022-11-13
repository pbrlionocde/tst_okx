# type: ignore
import base64
import hmac
import json
import os
import typing as t

import requests

from api_wrappers.custom_exceptions import JSONParseError
from logger.logger_conf import get_logger
from utilities.time import get_timestamp


class OkxClientBase:
    """
    Credentials to OKX API `trade_bot`
    """

    _rest_domain = 'https://www.okx.com'
    _demo_header = {'x-simulated-trading': '1'}
    _demo_mode: bool # Set through DEMO_MODE env variable to work in the demo network

    logger = get_logger()

    def __init__(self, *args, **kwargs):
        self.__access_key = os.environ['API_KEY']
        self.__api_passphrase = os.environ['API_PASSPHRASE']
        self.__api_secret = os.environ['API_SECRET_KEY']

    def __get_signature(self, timestamp: str, method: str, request_path: str):
        creds = f'{timestamp}{method}{request_path}'
        digest_mac = hmac.new(bytes(self.__api_secret, 'utf8'), msg=bytes(creds, 'utf8'), digestmod='sha256').digest()
        return base64.b64encode(digest_mac)

    def _get_private_request_headers(self, method: str, request_path: str):
        timestamp = get_timestamp()
        return {
            'OK-ACCESS-KEY': self.__access_key,   # The APIKey as a String.
            'OK-ACCESS-SIGN': self.__get_signature(timestamp, method, request_path),    # SHA256 signature
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-PASSPHRASE': self.__api_passphrase,
        }

    def execute_request(
        self,
        url,
        method,
        demo: bool = False,
        authorization: bool = False,
        body: t.Any = {},
        headers: t.Dict[str, str] = {},
    ):
        request_params = {
            'method': method,
            'url': f'{self._rest_domain}{url}',
            'headers': {},
        }
        if authorization:
            request_params['headers'].update(self._get_private_request_headers(method, url))
        if self._demo_mode:
            request_params['headers'].update(self._demo_header)
        request_params['headers'].update(headers)
        try:
            response = requests.request(**request_params)
        except Exception as e:
            self.logger.exception('error')
            return
        return response

    def parse_response(self, response) -> t.Dict:
        try:
            loaded = json.loads(response.content)
        except TypeError:
            self.logger.exception("This response can't be deserialized!")
            raise JSONParseError()

        return loaded


class OkxClient(OkxClientBase):
    """
    Use this class when make request to OKX.
    """

    def __init__(self, *args, **kwargs):
        self._demo_mode = bool(os.environ['DEMO_MODE'])
        super().__init__(*args, **kwargs)

    def get_account_balance(self, demo: bool = False):
        url = '/api/v5/account/balance'
        method = 'GET'
        resp = self.execute_request(url, method, authorization=True, demo=demo)
        return resp
