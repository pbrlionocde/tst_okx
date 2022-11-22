import os

from api_wrappers.base.okx import OkxClientBase
from api_wrappers.models import InitializeModels

initializer = InitializeModels(module='market')


class OkxMarketClient(OkxClientBase):
    """
    Use this class when make request to OKX.
    """

    def __init__(self, *args, **kwargs):
        self._demo_mode = bool(os.environ['DEMO_MODE'])
        super().__init__(*args, **kwargs)

    def get_market_price(
        self,
        inst_type: str = 'FUTURES',
        uly: str = 'FUTURES',
        inst_id: str = 'ETH-USD-221125',
        load: bool = False,
    ):
        url = '/api/v5/public/mark-price'
        method = 'GET'
        resp = self.execute_request(
            url,
            method,
            authorization=False,
            query={
                'instType': inst_type,
                # 'uly': uly,   Check this parameter in the documentation
                'instId': inst_id,
            },
        )
        if load:
            balance_model = initializer('MarketPrice')
            return self.load_data(resp, balance_model)
        return resp
