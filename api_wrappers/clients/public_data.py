import os

from api_wrappers.base.okx import OkxClientBase
from api_wrappers.models import InitializeModels

initializer = InitializeModels(module='public_data')


class OkxPublicDataClient(OkxClientBase):
    """
    Use this class when make request to OKX.
    """

    def __init__(self, *args, **kwargs):
        self._demo_mode = bool(os.environ['DEMO_MODE'])
        super().__init__(*args, **kwargs)

    def get_instruments(self, inst_type: str = 'FUTURES', load: bool = True):
        url = '/api/v5/public/instruments'
        method = 'GET'
        resp = self.execute_request(url, method, authorization=True, query={'instType': inst_type})
        if load:
            instrument_model = initializer('InstrumentPublicData')
            return self.load_data(resp['data'], instrument_model, many=True)
        return resp
