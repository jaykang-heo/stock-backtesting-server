from pydantic import BaseModel


class SigmaOrder(BaseModel):
    period: int
    line: int
