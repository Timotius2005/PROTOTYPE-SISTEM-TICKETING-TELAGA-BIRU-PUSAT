from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.sync import SyncLogCreate, SyncLogOut, SyncData, SyncResponse
from app.crud import sync_crud
from app.api.deps import get_db
from app.services.sync_services import handle_sync

router = APIRouter()

@router.post("/", response_model=SyncLogOut)
def create_sync_log(sync_log: SyncLogCreate, db: Session = Depends(get_db)):
    return sync_crud.create_sync_log(db, sync_log)

@router.get("/", response_model=List[SyncLogOut])
def read_all_sync_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return sync_crud.get_all_sync_logs(db, skip=skip, limit=limit)

@router.get("/{sync_log_id}", response_model=SyncLogOut)
def read_sync_log(sync_log_id: int, db: Session = Depends(get_db)):
    db_log = sync_crud.get_sync_log_by_id(db, sync_log_id)
    if not db_log:
        raise HTTPException(status_code=404, detail="Sync log not found")
    return db_log

@router.post("/sync", response_model=SyncResponse)
def sync_data(
    data: SyncData,
    db: Session = Depends(get_db)
):
    try:
        return handle_sync(data, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sync failed: {e}")
