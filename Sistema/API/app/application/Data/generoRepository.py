from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.GeneroModel import Genero,GeneroSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
from ..Shared import db
generoSchema = GeneroSchema()

# session = SessionManager.getInstance()
engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# # create a Session
Session = sessionmaker(engine)
session = db.session

def get_genero(id):    
    with Session() as session:
        genero = session.query(Genero).filter(Genero.id == id).first()
    return genero

def query_genero():
    with Session() as session:
        genero = session.query(Genero).all()
    return genero

def genero_create(genero):
    session.add(genero)
    session.commit()

def genero_update(genero):
    currentGenero = session.query(Genero).filter(Genero.id == genero.id).first()
    currentGenero.nombre = genero.nombre
    session.add(currentGenero)
    session.commit()

def genero_delete(id):
    try:
        session.query(Genero).filter(Genero.id == id).delete()
    except:
        raise ValueError('Error al eliminar un genero')
    finally:
        session.commit()