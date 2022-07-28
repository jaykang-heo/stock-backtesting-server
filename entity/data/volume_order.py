from pydantic import BaseModel


class VolumeOrder(BaseModel):
    limit: int
    ascending: bool

