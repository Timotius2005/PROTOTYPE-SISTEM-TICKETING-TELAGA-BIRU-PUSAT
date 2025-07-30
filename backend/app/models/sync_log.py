from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from app.core.session import Base

class SyncLog(Base):
    __tablename__ = "sync_logs"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False)  
    data_type = Column(String, nullable=False)
    data_content = Column(Text, nullable=True)
    success = Column(Boolean, default=False)  
    detail = Column(Text, nullable=True)  
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    message = Column(Text, nullable=True)  
