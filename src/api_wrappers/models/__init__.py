
"""
Import from this package should be as in the example below:
    from src.api_wrappers.models import InitializeModels

    initializer = InitializeModels()
    your_model_instance = initializer('YourModelName')

!!! `your_model_instance` has all methods `marshmallow.Schema` !!!

Please read the documentation about using marshmallow Schema:
https://marshmallow.readthedocs.io/en/stable/
"""
from typing import Final, Type

import marshmallow

BASE_PATH: Final = 'src.api_wrappers.models.'


class InitializeModels:
    def __init__(self, import_model_names: str = (), module: str = ''):
        self.import_model_names = import_model_names
        self.module = module

    def __call__(self, model_name: str, module: str = '') -> Type[marshmallow.Schema]:
        if self.import_model_names and model_name not in self.import_model_names:
            raise ImportError(f'`{model_name}` does not exist in the models package or was restricted in initializer')
        if not module:
            assert self.module, 'You must specify a module when __init__ or __call__ method is called'  # noqa: S101
            module = self.module
        model_class = __import__(f'{BASE_PATH}{module}', fromlist=[model_name])
        return getattr(model_class, model_name)


__all__ = [
    'InitializeModels',
]
