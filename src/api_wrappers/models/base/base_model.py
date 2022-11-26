from typing import Type

from marshmallow import Schema


class BaseModel:
    Schema: Type[Schema]

    @classmethod
    def load(cls, data, many: bool = False):
        return cls.Schema().load(data=data, many=many)

    def dump(self):
        return self.Schema().dump(self)
