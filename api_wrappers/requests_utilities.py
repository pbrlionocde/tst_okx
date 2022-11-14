import typing as t


def join_query(query_params: t.Dict[str, str]) -> str:
    return '?' + '&'.join([f'{key}={value}' for key, value in query_params.items()])


class MetaChecker:      # TODO: Add checks to an existing method
    def __new__(cls, name, bases, dct):
        inst = type(name, bases, dct)
        # assert getattr(inst, '_get_private_request_headers', None) is not None, 'Use only for inheritance'
        return inst


class SetupAPIKwargs(metaclass=MetaChecker):
    _demo_mode: bool # Set through DEMO_MODE env variable to work in the demo network
    __kwargs_keys = (
        '_method',
        '_url',
        '_query',
        '_authorization',
        '_body',
        '_headers',
    )

    def __init__(self, domain):
        self.domain = domain

    def get_request_kwargs(self, **kwargs):
        """You must provide all arguments as keyword arguments"""
        self.kwargs = kwargs
        request_params = self.__process_arguments()
        if self._demo_mode:
            request_params['headers'].update(self._demo_header)
        return request_params

    def __process_arguments(self):
        request_params = {
            'url': '',
            'method': '',
            'headers': dict(),
            'data': dict(),
        }
        for key in self.__kwargs_keys:
            getattr(self, key)(request_params=request_params)
        return request_params

    def _method(self, request_params):
        request_params['method'] = self.kwargs['method'].upper()

    def _url(self, request_params):
        request_params['url']=f'{self.domain}{self.kwargs["url"]}'

    def _authorization(self, request_params):
        request_path = self.kwargs['url']
        if query_params := self.kwargs.get('query'):
            request_path += join_query(query_params)
        request_params['headers'].update(
            self._get_private_request_headers(
                method=self.kwargs['method'],
                request_path=request_path,
            ),
        )

    def _query(self, request_params):
        if query_params := self.kwargs.get('query'):
            request_params['url'] += join_query(query_params)

    def _body(self, request_params):
        request_params['data'] = self.kwargs.get('body', dict())

    def _headers(self, request_params):
        request_params['headers'].update(self.kwargs.get('headers', dict))
