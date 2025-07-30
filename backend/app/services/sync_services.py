import logging
from app.schemas.sync import SyncData, SyncResponse
from sqlalchemy.orm import Session
from app.models.tickets import Ticket
from app.models.sync_log import SyncLog
from datetime import datetime
from app.crud import ticket_crud
from app.schemas.tickets import TicketCreate

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def handle_sync(data: SyncData, db: Session):
    if data.data_type == "ticket":
        for idx, ticket_data in enumerate(data.data_content):
            logging.info(f"Processing ticket {idx + 1}: {ticket_data}")
            try:
                existing = db.query(Ticket).filter_by(id=ticket_data.id).first()
                if existing:
                    logging.info(f"Ticket with ID {ticket_data.id} already exists. Skipping.")
                    continue
                ticket_crud.create_ticket(db=db, ticket=ticket_data)
                logging.info(f"Ticket with ID {ticket_data.id} successfully created.")
            except Exception as e:
                logging.error(f"Failed to create ticket with ID {getattr(ticket_data, 'id', 'unknown')}: {e}")
    try:
        log = SyncLog(
            source=data.source,
            success=True,
            data_type=data.data_type
        )
        db.add(log)
        db.commit()
        logging.info(f"Sync log added for source: {data.source}")
    except Exception as e:
        logging.error(f"Failed to add sync log: {e}")
    return SyncResponse(success=True, message="Sync completed successfully")