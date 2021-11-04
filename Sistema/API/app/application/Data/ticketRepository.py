from typing import final
from sqlalchemy.orm import session

from ..Model.TicketModel import Ticket
from ..connection_manager import SessionManager
from ..Model.PeliculaModel import Pelicula,PeliculaSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
from ..Shared import db
peliculaSchema = PeliculaSchema()

# session = SessionManager.getInstance()
engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
Session = sessionmaker(engine)
session = db.session
def create_ticket(ticket):
        session.add(ticket)
        session.commit()
        return ticket.id

def get_ticket(id):
        return session.query(Ticket).filter(Ticket.id == id).first()