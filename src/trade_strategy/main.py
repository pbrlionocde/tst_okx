from datetime import datetime

from src.trading_view_wrapper.analyze import Analyzer
from src.api_wrappers.models import InitializeModels

initalizer = InitializeModels(module='trade')

request_order_model = initalizer(model_name='TradeOrderRequest')


class LastOrder:
    def __init__(self, order_type: str, order_amount: float):
        self.type: str = order_type
        self.datetime: datetime = datetime.now()
        self.amount: float = order_amount
        # TODO: invoke save celery task!


class Trade:
    _buy_key: str = 'buy'
    _sell_key: str = 'sell'
    analyzer = Analyzer()

    def __init__(self, inst_id: str):
        self.inst_id = inst_id

    def save_history(self):
        pass

    def buy(self, quantity: float):
        order_instance = request_order_model(
            sz=quantity,
            side=self._sell_key,
            inst_id=self.inst_id,
            td_mode='isolated',
            ord_type='market',
        )

    def sell(self):
        pass

    def get_forecast(self):
        for full_forecast in self.analyzer():
            yield full_forecast['prognose'] # TODO: setup key

    def run(self):
        for forecast in self.get_forecast():
            pass

    @property
    def order_price(self):
        # TODO: generate price by market_client

