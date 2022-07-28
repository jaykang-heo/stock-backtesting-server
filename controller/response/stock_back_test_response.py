from dataclasses import dataclass

from typing import List

from entity.data.condition import Condition


@dataclass
class StockBackTestResponse:
    date: int
    percentage: float
    stock_codes: List[str]

