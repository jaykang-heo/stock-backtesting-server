from pydantic import BaseModel


class CciOrder(BaseModel):
    period: int
    line: int
