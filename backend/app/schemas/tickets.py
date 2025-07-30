from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TicketBase(BaseModel):
    id: int
    regular_qty: int = 0
    vip_qty: int = 0
    vvip_qty: int = 0
    total_price: float
    is_synced: Optional[bool] = True


class TicketCreate(TicketBase):
    pass


class TicketResponse(TicketBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
