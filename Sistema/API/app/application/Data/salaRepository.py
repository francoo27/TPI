
from ..Model.SalaModel import Sala,SalaSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from config import DevConfig
from ..Shared import db
salaSchema = SalaSchema()

engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(engine)
session = db.session

def get_sala(id):    
    sala = session.query(Sala).filter(Sala.id == id).first()
    return sala

def query_sala():
    sala = session.query(Sala).all()
    return sala

def query_sala_byComplejo(complejoId):
    sala = session.query(Sala).filter(Sala.id_complejo == complejoId).all()
    return sala
    