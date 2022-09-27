from pydantic import BaseModel


class CciOrder(BaseModel):
    date: int
    period: int
    line: int
    # true= greater or equal false= less
    operator: bool
