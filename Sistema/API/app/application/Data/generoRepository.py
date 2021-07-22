from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.GeneroModel import Genero,GeneroSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
generoSchema = GeneroSchema()

engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(engine)

def get_genero(id):    
    with Session() as session:
        genero = session.query(Genero).filter(Genero.id == id).first()
    return genero

def query_genero():
    with Session() as session:
        genero = session.query(Genero).all()
    return genero