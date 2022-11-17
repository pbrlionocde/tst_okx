
"""
Import from this package should be as in the example below:
    from api_wrappers.models import InitializeModels

    initializer = InitializeModels()
    your_model_instance = initializer('YourModelName')

!!! `your_model_instance` has all methods `marshmallow.Schema` !!!

Please read the documentation about using marshmallow Schema:
https://marshmallow.readthedocs.io/en/stable/
"""

from api_wrappers.models.account import *
from typing import Type
from marshmallow_dataclass import class_schema
import marshmallow

IMPORT_MODEL_NAMES = [
    *account_model_names()
]


class InitializeModels:
    def __init__(self, import_model_names: str = IMPORT_MODEL_NAMES):
        self.import_model_names = import_model_names

    def __call__(self, model_name: str) -> Type[marshmallow.Schema]:
        if model_name not in self.import_model_names:
            raise ImportError(f'`{model_name}` does not exist in the models package or was restricted in initializer')
        model_class = globals()[model_name]
        return class_schema(model_class)()


__all__ = [
    'InitializeModels',
]
