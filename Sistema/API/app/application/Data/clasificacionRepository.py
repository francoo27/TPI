from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.ClasificacionModel import Clasificacion,ClasificacionSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
from ..Shared import db
clasificacionSchema = ClasificacionSchema()

engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# # create a Session
Session = sessionmaker(engine)
session = db.session

def get_clasificacion(id):    
    with Session() as session:
        clasificacion = session.query(Clasificacion).filter(Clasificacion.id == id).first()
    return clasificacion

def query_clasificacion():
    with Session() as session:
        clasificacion = session.query(Clasificacion).all()
    return clasificacion

def clasificacion_create(clasificacion):
    session.add(clasificacion)
    session.commit()

def clasificacion_update(clasificacion):
    currentClasificacion = session.query(Clasificacion).filter(Clasificacion.id == clasificacion.id).first()
    currentClasificacion.identificador = clasificacion.identificador
    currentClasificacion.edadMinima = clasificacion.edadMinima
    currentClasificacion.recomendacion = clasificacion.recomendacion
    currentClasificacion.definicion = clasificacion.definicion
    session.add(currentClasificacion)
    session.commit()

def clasificacion_delete(id):
    try:
        session.query(Clasificacion).filter(Clasificacion.id == id).delete()
    except:
        raise ValueError('Error al eliminar una clasificacion')
    finally:
        session.commit()