from pydantic import BaseModel


class AmountOrder(BaseModel):
    limit: int
    ascending: bool
