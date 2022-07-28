from pydantic import BaseModel


class PsarOrder(BaseModel):
    acceleration: float
    maximum: float
    upper: bool
