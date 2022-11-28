

class BaseModel:
    @classmethod
    def load(cls, data, many: bool = False):
        return cls.Schema().load(data=data, many=many)
