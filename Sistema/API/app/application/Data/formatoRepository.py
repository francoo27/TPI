from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.FormatoModel import Formato,FormatoSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
from ..Shared import db
formatoSchema = FormatoSchema()

session = db.session

def get_formato(id):    
    formato = session.query(Formato).filter(Formato.id == id).first()
    return formato

def get_formato_by_name(name):
    return session.query(Formato).filter(Formato.nombre == name).first()

def query_formato():
    formato = session.query(Formato).all()
    return formato

def formato_create(formato):
        session.add(formato)
        session.commit()

def formato_update(formato):
    currentFormato = session.query(Formato).filter(Formato.id == formato.id).first()
    currentFormato.nombre = formato.nombre
    session.add(currentFormato)
    session.commit()

def formato_delete(id):
    try:
        session.query(Formato).filter(Formato.id == id).delete()
    except:
        raise ValueError('Error al eliminar una formato')
    finally:
        session.commit()
