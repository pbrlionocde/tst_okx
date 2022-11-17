# type: ignore
import base64
import hmac
import json
import os
import typing as t

import requests
from marshmallow import Schema

from api_wrappers.custom_exceptions import JSONParseError
from api_wrappers.models import InitializeModels
from api_wrappers.requests_utilities import SetupAPIKwargs
from logger.logger_conf import get_logger
from utilities.time import get_timestamp

initializer = InitializeModels()


class OkxClientBase(SetupAPIKwargs):
    """
    Credentials to OKX API `trade_bot`
    """

    _rest_domain = 'https://www.okx.com'
    _demo_header = {'x-simulated-trading': '1'}
    logger = get_logger()

    def __init__(self, *args, **kwargs):
        self.__access_key = os.environ['API_KEY']
        self.__api_passphrase = os.environ['API_PASSPHRASE']
        self.__api_secret = os.environ['API_SECRET_KEY']
        super().__init__(self._rest_domain)

    def __get_signature(self, timestamp: str, method: str, request_path: str):
        msg = f'{timestamp}{method}{request_path}'
        digest_mac = hmac.new(bytes(self.__api_secret, 'utf8'), msg=bytes(msg, 'utf8'), digestmod='sha256').digest()
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
        authorization: bool = False,
        body: t.Any = {},
        headers: t.Dict[str, str] = {},
        query: t.Dict[str, str] = {},
    ):
        try:
            response = requests.request(**self.get_request_kwargs(
                url=url,
                method=method,
                authorization=authorization,
                body=body,
                headers=headers,
                query=query,
            ))
        except Exception:
            self.logger.exception('error')
            return
        return response

    def parse_response(self, response) -> t.Dict:
        try:
            loaded = json.loads(response.content)
        except TypeError:
            self.logger.exception("This response can't be deserialized as json!")
            raise JSONParseError()
        return loaded

    def load_data(self, response: t.Dict[str, t.Any], model: Schema):
        parsed_data = self.parse_response(response)
        return model.load(data=parsed_data)


class OkxClient(OkxClientBase):
    """
    Use this class when make request to OKX.
    """

    def __init__(self, *args, **kwargs):
        self._demo_mode = bool(os.environ['DEMO_MODE'])
        super().__init__(*args, **kwargs)

    def get_account_balance(self, symbol: str = 'BTC', load: bool = True):
        url = '/api/v5/account/balance'
        method = 'GET'
        resp = self.execute_request(url, method, authorization=True, query={'ccy': symbol})
        if load:
            balance_model = initializer('Balance')
            return self.load_data(resp, balance_model)
        return resp
