from typing import TypedDict

Metadata = TypedDict(
    'Metadata',
    {
        'data_key': str,
        'required': bool,
    },
    total=False,
)
