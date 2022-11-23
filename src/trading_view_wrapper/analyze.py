from datetime import datetime
from time import sleep

from tradingview_ta import Interval, TA_Handler

from src.trading_view_wrapper.common.interval import Interval as WrappedInterval
from src.trading_view_wrapper.exceptions import BrokenInterfaceAccessError


class Analyzer(TA_Handler):
    _initialized_handler = None

    def __init__(
        self,
        screener='',
        exchange='',
        symbol='',
        interval='',
        timeout=None,
        proxies=None,
    ):
        self.wrapped_interval = WrappedInterval(Interval.INTERVAL_1_MINUTE if not interval else interval)
        screener = 'crypto' if not screener else screener
        exchange = 'OKX' if not exchange else exchange
        symbol = 'ETHUSDT' if not symbol else symbol
        super().__init__(screener, exchange, symbol, self.wrapped_interval.time_value, timeout, proxies)

    @property
    def initialized_handler(self):
        if not self._initialized_handler:
            raise BrokenInterfaceAccessError('Use only `__call__` interface to access this class!')
        return self._initialized_handler

    @initialized_handler.setter
    def initialized_handler(self, value):
        self._initialized_handler = value

    def __call__(cls, *args, **kwds):
        cls.initialized_handler = cls  # TODO: Explore more reliable initialization
        while True:
            # start_time = datetime.now()
            yield cls.initialized_handler.get_analysis().summary
            # cls.wait(start_time=start_time)

    def wait(self, start_time: datetime) -> None:
        expired_time = datetime.now() - start_time
        expired_time = int(expired_time.seconds)
        if expired_time > self.wrapped_interval.sleep_time:
            return None
        sleep(self.wrapped_interval.sleep_time - expired_time)
