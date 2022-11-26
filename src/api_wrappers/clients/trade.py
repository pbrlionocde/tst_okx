import typing as t

from src.api_wrappers.base.okx import OkxClientBase
from src.api_wrappers.models import InitializeModels
from src.api_wrappers.models.base.base_model import BaseModel

initializer = InitializeModels(module='trade')


class OkxTradeClient(OkxClientBase):
    """
    Use this class when make request to OKX.
    """

    def place_order(self, order_instance: t.Type[BaseModel], load: bool = True):
        url = '/api/v5/trade/order'
        method = 'POST'
        body = order_instance.dump()
        resp = self.execute_request(url, method, authorization=True, body=body)
        if load:
            order_response_model = initializer('TradeOrderResponse')
            return self.load_data(resp['data'], order_response_model, many=True)
        return resp
