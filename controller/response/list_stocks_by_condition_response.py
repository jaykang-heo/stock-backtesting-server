from typing import List

from pydantic import BaseModel


class ListStocksByConditionResponse(BaseModel):
    date: int
    codes: List[str]
