from dataclasses import dataclass

from typing import List

from entity.data.Filter import Filter


@dataclass
class StockBackTestResponse:
    date: int
    percentage: float
    stockCodes: List[str]

