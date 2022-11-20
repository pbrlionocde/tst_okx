from typing import Dict


def join_query(query_params: Dict[str, str]) -> str:
    return '?' + '&'.join([f'{key}={param}' for key, param in query_params.items()])
