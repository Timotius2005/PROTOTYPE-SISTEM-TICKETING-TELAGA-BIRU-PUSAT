import json
from sqlalchemy.orm import Session
from app.models.sync_log import SyncLog
from app.schemas.sync import SyncLogCreate

def create_sync_log(db: Session, sync_log: SyncLogCreate):
    db_sync_log = SyncLog(
        source=sync_log.source,
        data_type=sync_log.data_type,
        data_content=json.dumps(sync_log.data_content),
        success=sync_log.success,
        message=sync_log.message,
    )
    db.add(db_sync_log)
    db.commit()
    db.refresh(db_sync_log)
    return db_sync_log

def get_all_sync_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SyncLog).offset(skip).limit(limit).all()

def get_sync_log_by_id(db: Session, sync_log_id: int):
    return db.query(SyncLog).filter(SyncLog.id == sync_log_id).first()