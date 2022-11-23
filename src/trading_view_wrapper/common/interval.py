
from typing import Final

# from functools import cached_property TODO: Investigate `sleep_time`` working time
from src.trading_view_wrapper.exceptions import AccessToInitializeError, InvalidIntervalValueError

INTERVALS: Final = {
    '1m': 60,
    '5m': 60 * 5,
    '15m': 60 * 15,
    '30m': 60 * 30,
    '1h': 60 * 60,
    '2h': 60 * 60 * 2,
    '4h': 60 * 60 * 4,
    '1d': 60 * 60 * 24,
    '1W': 60 * 60 * 24 * 7,
    '1M': 60 * 60 * 24 * 7 * 30,
}


class Interval(object):
    _sleep_time = None

    def __init__(self, interval: str) -> None:
        self.time_value = interval
        self.sleep_time = interval

    @property
    def sleep_time(self):
        if not self._sleep_time:
            raise AccessToInitializeError('Raise when try to access before initialize data')
        return self._sleep_time

    @sleep_time.setter
    def sleep_time(self, value):
        self._sleep_time = self.get_sleep_time_by_interval(value)

    @classmethod
    def get_sleep_time_by_interval(cls, interval: str) -> int:
        if isinstance(interval, str) and (seconds := INTERVALS.get(interval)):
            return seconds
        raise InvalidIntervalValueError(f'Invalid interval: {interval}')
