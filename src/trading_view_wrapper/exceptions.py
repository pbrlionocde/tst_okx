class BrokenInterfaceAccessError(Exception):
    """Use only `__call__` interface to access this class!"""


class InvalidIntervalValueError(Exception):
    """Raise when interval does not exist in `INTERVALS`"""


class AccessToInitializeError(Exception):
    """Raise when try to access before initialize data"""


class RecommendationError(Exception):
    """Raise when recommendation does not exist"""
