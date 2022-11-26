from src.api_wrappers.base.okx import OkxClientBase
from src.api_wrappers.models import InitializeModels

initializer = InitializeModels(module='market')


class OkxMarketClient(OkxClientBase):
    """
    Use this class when make request to OKX.
    """

    def get_market_price(
        self,
        inst_id: str,
        inst_type: str = 'FUTURES',
        uly: str = 'FUTURES',
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
