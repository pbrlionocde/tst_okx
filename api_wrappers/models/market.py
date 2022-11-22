from dataclasses import dataclass, field

from marshmallow import pre_load

from api_wrappers.models.common.metadata import Metadata


@dataclass
class MarketPrice:
    inst_id: str = field(metadata=Metadata(data_key='instId'))
    inst_type: str = field(metadata=Metadata(data_key='instType'))
    mark_px: float = field(metadata=Metadata(data_key='markPx'))
    ts: str

    @pre_load
    def load_from_list(self, data, many, **kwargs):
        return data['data'][0]


__all__ = (
    'MarketPrice',
)
