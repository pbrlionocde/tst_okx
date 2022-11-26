from src.api_wrappers.base.okx import OkxClientBase
from src.api_wrappers.models import InitializeModels

initializer = InitializeModels(module='account')


class OkxAccountClient(OkxClientBase):
    """
    Use this class when make request to OKX.
    """

    def get_account_balance(self, symbol: str = 'BTC', load: bool = True):
        url = '/api/v5/account/balance'
        method = 'GET'
        resp = self.execute_request(url, method, authorization=True, query={'ccy': symbol})
        if load:
            balance_model = initializer('AccountBalance')
            return self.load_data(resp, balance_model)
        return resp
