from dataclasses import dataclass, field
from typing import List

from api_wrappers.models.metadata import Metadata


# Balance
@dataclass
class InstrumentPublicData:
    alias: str
    base_ccy: str = field(metadata=Metadata(data_key='baseCcy',))
    category: str
    ct_mult: str = field(metadata=Metadata(data_key='ctMult'))
    ct_type: str = field(metadata=Metadata(data_key='ctType'))
    ct_val: str = field(metadata=Metadata(data_key='ctVal'))
    ct_val_ccy: str = field(metadata=Metadata(data_key='ctValCcy'))
    exp_time: str = field(metadata=Metadata(data_key='expTime'))
    inst_family: str = field(metadata=Metadata(data_key='instFamily'))
    inst_id: str = field(metadata=Metadata(data_key='instId'))
    inst_type: str = field(metadata=Metadata(data_key='instType'))
    lever: str
    list_ime: str = field(metadata=Metadata(data_key='listTime'))
    lot_sz: str = field(metadata=Metadata(data_key='lotSz'))
    max_iceberg_sz: str = field(metadata=Metadata(data_key='maxIcebergSz'))
    max_lmt_sz: str = field(metadata=Metadata(data_key='maxLmtSz'))
    max_mkt_sz: str = field(metadata=Metadata(data_key='maxMktSz'))
    max_stop_sz: str = field(metadata=Metadata(data_key='maxStopSz'))
    max_trigger_sz: str = field(metadata=Metadata(data_key='maxTriggerSz'))
    max_twap_sz: str = field(metadata=Metadata(data_key='maxTwapSz'))
    min_sz: str = field(metadata=Metadata(data_key='minSz'))
    opt_type: str = field(metadata=Metadata(data_key='optType'))
    quote_ccy: str = field(metadata=Metadata(data_key='quoteCcy'))
    settle_ccy: str = field(metadata=Metadata(data_key='settleCcy'))
    state: str
    stk: str
    tickSz: str = field(metadata=Metadata(data_key='tickSz'))
    uly: str
