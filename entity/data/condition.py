from typing import List

from pydantic import BaseModel

from entity.data import volume_order, sigma_order, psar_order, changerate_order, cci_order, amount_order
from entity.data.amount_order import AmountOrder
from entity.data.cci_order import CciOrder
from entity.data.changerate_order import ChangeRateOrder
from entity.data.psar_order import PsarOrder
from entity.data.sigma_order import SigmaOrder
from entity.data.volume_order import VolumeOrder


class Condition(BaseModel):
    date: int
    volume_orders: List[VolumeOrder]
    amount_orders: List[AmountOrder]
    sigma_orders: List[SigmaOrder]
    psar_orders: List[PsarOrder]
    change_rate_orders: List[ChangeRateOrder]
    cci_orders: List[CciOrder]
