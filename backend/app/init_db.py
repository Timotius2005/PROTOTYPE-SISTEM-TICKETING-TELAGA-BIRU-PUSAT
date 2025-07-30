from app.core.session import engine
from app.models import tickets
from app.models import sync_log

tickets.Base.metadata.create_all(bind=engine)
sync_log.Base.metadata.create_all(bind=engine)
