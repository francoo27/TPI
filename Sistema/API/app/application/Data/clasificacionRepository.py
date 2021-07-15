from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.ClasificacionModel import Clasificacion,ClasificacionSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
clasificacionSchema = ClasificacionSchema()

engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(engine)

def get_clasificacion(id):    
    with Session() as session:
        clasificacion = session.query(Clasificacion).filter(Clasificacion.id == id).first()
    return clasificacion

def query_clasificacion():
    with Session() as session:
        clasificacion = session.query(Clasificacion).all()
    return clasificacion