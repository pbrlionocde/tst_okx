

class JSONParseError(Exception):
    """Raises when content of response can't be deserialized!"""


class InstrumentDoesNotExistError(Exception):

    def __init__(self, url, inst_id: str):
        self.url = url
        self.inst_id = inst_id
        self.message = 'Instrument does not exist'
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'{self.url} -> {self.message}: {self.inst_id}'


class InstrumentDoesNotMatchError(Exception):

    def __init__(self, url, inst_id: str):
        self.url = url
        self.inst_id = inst_id
        self.message = 'Instrument does not match'
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'{self.url} -> {self.message}: {self.inst_id}'
