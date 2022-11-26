from dataclasses import field

from marshmallow_dataclass import dataclass

from src.api_wrappers.models.base.base_model import BaseModel
from src.api_wrappers.models.common.metadata import Metadata


@dataclass
class TradeOrderRequest(BaseModel):
    # https://www.okx.com/docs-v5/en/#rest-api-trade-place-order
    sz: str = field(metadata=Metadata(required=True))
    side: str = field(metadata=Metadata(required=True))
    inst_id: str = field(metadata=Metadata(data_key='instId', required=True))
    td_mode: str = field(metadata=Metadata(data_key='tdMode', required=True))
    ord_type: str = field(metadata=Metadata(data_key='ordType', required=True))
    px: str  # Order price. Only applicable to limit,post_only,fok,ioc order.
    ccy: str
    tag: str
    cl_ord_id: str = field(metadata=Metadata(data_key='clOrdId'))
    pos_side: str = field(metadata=Metadata(data_key='posSide'))
    reduce_only: str = field(metadata=Metadata(data_key='reduceOnly'))
    tgt_ccy: str = field(metadata=Metadata(data_key='tgtCcy'))
    ban_amend: str = field(metadata=Metadata(data_key='banAmend'))
    tp_trigger_px: str = field(metadata=Metadata(data_key='tpTriggerPx'))
    tp_ord_px: str = field(metadata=Metadata(data_key='tpOrdPx'))
    sl_trigger_px: str = field(metadata=Metadata(data_key='slTriggerPx'))
    sl_ord_px: str = field(metadata=Metadata(data_key='slOrdPx'))
    tp_trigger_px_type: str = field(metadata=Metadata(data_key='tpTriggerPxType'))
    sl_trigger_px_type: str = field(metadata=Metadata(data_key='slTriggerPxType'))


@dataclass
class TradeOrderResponse(BaseModel):
    tag: str
    ord_id: str = field(metadata=Metadata(data_key='ordId'))
    cl_ord_id: str = field(metadata=Metadata(data_key='clOrdId'))
    s_code: str = field(metadata=Metadata(data_key='sCode'))
    s_msg: str = field(metadata=Metadata(data_key='sMsg'))
