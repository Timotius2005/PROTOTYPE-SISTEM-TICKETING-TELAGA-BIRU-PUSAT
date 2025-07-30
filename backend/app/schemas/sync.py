from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime
from app.schemas.tickets import TicketCreate
from typing import List

class SyncLogBase(BaseModel):
    source: str
    data_type: str
    data_content: Any
    success: Optional[bool] = False
    message: Optional[str] = None

class SyncLogCreate(SyncLogBase):
    pass

class SyncLogResponse(SyncLogBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
class SyncResponse(BaseModel):
    success: bool
    message: Optional[str] = None

class SyncLogOut(SyncLogBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class SyncData(BaseModel):
    source: str  
    data_type: str  
    data_content: List[TicketCreate]  