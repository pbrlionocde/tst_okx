# type: ignore
import base64
import hmac
import json
import os
import typing as t

import requests

from src.api_wrappers.base.requests_utilities import SetupAPIKwargs
from src.api_wrappers.exceptions.process_error_responses import ErrorProcessorMixin
from src.api_wrappers.models.base.base_model import BaseModel
from src.api_wrappers.utils import custom_exceptions
from src.logger.logger_conf import get_logger
from src.utilities.time import get_timestamp

EXCEPTION_CODES: t.Final = {
    '51001': custom_exceptions.InstrumentDoesNotExistError,
    '51015': custom_exceptions.InstrumentDoesNotMatchError,
    '50001': custom_exceptions.ServiceTemporarilyUnavailableError,
}


class OkxClientBase(ErrorProcessorMixin):
    """
    Credentials to OKX API `trade_bot`
    """
    _rest_domain = 'https://www.okx.com'

    def __init__(self, *args, **kwargs):
        self.__access_key = os.environ['API_KEY']
        self.__api_passphrase = os.environ['API_PASSPHRASE']
        self.__api_secret = os.environ['API_SECRET_KEY']
        self._demo_mode = bool(os.environ['DEMO_MODE'])
        self.logger = get_logger()

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
        body: t.Any = dict(),   # noqa: C408, B006
        headers: t.Dict[str, str] = dict(),   # noqa: C408, B006
        query: t.Dict[str, str] = dict(),   # noqa: C408, B006
    ):
        request_arguments = SetupAPIKwargs(self._rest_domain, self._get_private_request_headers, demo=self._demo_mode)
        try:
            response = requests.request(**request_arguments.get_request_kwargs(
                url=url,
                method=method,
                authorization=authorization,
                body=body,
                headers=headers,
                query=query,
            ))
        except Exception:
            self.logger.exception('error')
            raise
        else:
            parsed_content = self.parse_response(response)
            if exception := EXCEPTION_CODES.get(parsed_content['code']):
                self._process_error_response(exception, url=url, inst_id=query['instId'])
        return parsed_content

    def parse_response(self, response: t.Type[requests.Response]) -> t.Dict:
        try:
            loaded = json.loads(response.content)
        except TypeError:
            self.logger.exception("This response can't be deserialized as json!")
            raise custom_exceptions.JSONParseError()
        return loaded

    def load_data(self, response: t.Dict[str, t.Any], model: t.Type[BaseModel], many: bool = False):
        return model.load(data=response, many=many)
