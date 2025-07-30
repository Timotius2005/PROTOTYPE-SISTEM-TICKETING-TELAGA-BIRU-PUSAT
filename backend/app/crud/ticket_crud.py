from sqlalchemy.orm import Session
from app.models.tickets import Ticket
from app.schemas.tickets import TicketCreate

def create_ticket(db: Session, ticket: TicketCreate):
    db_ticket = Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
