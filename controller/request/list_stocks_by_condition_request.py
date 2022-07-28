from typing import List

from pydantic import BaseModel

from entity.data.amount_order import AmountOrder
from entity.data.cci_order import CciOrder
from entity.data.changerate_order import ChangeRateOrder
from entity.data.psar_order import PsarOrder
from entity.data.sigma_order import SigmaOrder
from entity.data.volume_order import VolumeOrder


class ListStocksByConditionRequest(BaseModel):
    date: int
    volume_orders: List[VolumeOrder]
    amount_orders: List[AmountOrder]
    changerate_orders: List[ChangeRateOrder]
    cci_orders: List[CciOrder]
    psar_orders: List[PsarOrder]
    sigma_orders: List[SigmaOrder]
