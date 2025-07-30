from sqlalchemy import Column, Integer, Float, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.session import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    regular_qty = Column(Integer, default=0)
    vip_qty = Column(Integer, default=0)
    vvip_qty = Column(Integer, default=0)
    total_price = Column(Float)
    is_synced = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())