from pydantic import BaseModel


class ChangeRateOrder(BaseModel):
    limit: int
    ascending: bool
