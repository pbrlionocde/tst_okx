from dataclasses import dataclass, field
from typing import List

from src.api_wrappers.models.common.metadata import Metadata


# Balance
@dataclass
class BalanceDataDetails:
    avail_bal: str = field(metadata=Metadata(data_key='availBal'))
    avail_eq: str = field(metadata=Metadata(data_key='availEq'))
    cash_bal: str = field(metadata=Metadata(data_key='cashBal'))
    ccy: str
    cross_liab: str = field(metadata=Metadata(data_key='crossLiab'))
    dis_eq: str = field(metadata=Metadata(data_key='disEq'))
    eq: str
    eq_usd: str = field(metadata=Metadata(data_key='eqUsd'))
    fixed_bal: str = field(metadata=Metadata(data_key='fixedBal'))
    frozen_bal: str = field(metadata=Metadata(data_key='frozenBal'))
    interest: str
    iso_eq: str = field(metadata=Metadata(data_key='isoEq'))
    iso_liab: str = field(metadata=Metadata(data_key='isoLiab'))
    iso_upl: str = field(metadata=Metadata(data_key='isoUpl'))
    liab: str
    max_loan: str = field(metadata=Metadata(data_key='maxLoan'))
    mgn_ratio: str = field(metadata=Metadata(data_key='mgnRatio'))
    notional_lever: str = field(metadata=Metadata(data_key='notionalLever'))
    ord_frozen: str = field(metadata=Metadata(data_key='ordFrozen'))
    spot_in_use_amt: str = field(metadata=Metadata(data_key='spotInUseAmt'))
    stgy_eq: str = field(metadata=Metadata(data_key='stgyEq'))
    twap: str
    u_time: str = field(metadata=Metadata(data_key='uTime'))
    upl: str
    upl_liab: str = field(metadata=Metadata(data_key='uplLiab'))


@dataclass
class BalanceData:
    adj_eq: str = field(metadata=Metadata(data_key='adjEq'))
    imr: str
    iso_eq: str = field(metadata=Metadata(data_key='isoEq'))
    mgn_ratio: str = field(metadata=Metadata(data_key='mgnRatio'))
    mmr: str
    notional_usd: str = field(metadata=Metadata(data_key='notionalUsd'))
    ord_froz: str = field(metadata=Metadata(data_key='ordFroz'))
    total_eq: str = field(metadata=Metadata(data_key='totalEq'))
    u_time: str = field(metadata=Metadata(data_key='uTime'))
    details: List[BalanceDataDetails]


@dataclass
class AccountBalance:
    code: str
    msg: str
    data: List[BalanceData]  # noqa: WPS120 # real item name


__all__ = (
    'AccountBalance',
    'BalanceData',
    'BalanceDataDetails',
)
