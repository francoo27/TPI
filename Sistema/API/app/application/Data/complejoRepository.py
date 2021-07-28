
from ..Model.ComplejoModel import Complejo,ComplejoSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from config import DevConfig
from ..Shared import db
complejoSchema = ComplejoSchema()

engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(engine)
session = db.session

def get_complejo(id):    
    complejo = session.query(Complejo).filter(Complejo.id == id).first()
    return complejo

def query_complejo():
    complejo = session.query(Complejo).all()
    return complejo

    