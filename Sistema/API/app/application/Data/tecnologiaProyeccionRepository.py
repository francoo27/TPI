from typing import final
from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.TecnologiaProyeccionModel import TecnologiaProyeccion,TecnologiaProyeccionSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
from ..Shared import db
tecnologiaproyeccionSchema = TecnologiaProyeccionSchema()

# session = SessionManager.getInstance()
engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
Session = sessionmaker(engine)
session = db.session
def tecnologia_proyeccion_create(tecnologiaproyeccion):
        session.add(tecnologiaproyeccion)
        session.commit()

def tecnologia_proyeccion_update(tecnologiaproyeccion):
    currentTecnologiaProyeccion = session.query(TecnologiaProyeccion).filter(TecnologiaProyeccion.id == tecnologiaproyeccion.id).first()
    currentTecnologiaProyeccion.nombre = tecnologiaproyeccion.nombre
    session.add(currentTecnologiaProyeccion)
    session.commit()

def query_tecnologia_proyeccion():
    tecnologiaproyeccion = session.query(TecnologiaProyeccion).all()
    return tecnologiaproyeccion

def tecnologia_proyeccion_delete(id):
    tecnologiaproyeccion = session.query(TecnologiaProyeccion).filter(TecnologiaProyeccion.id == id).first()
    tecnologiaproyeccion.formatos = []
    try:
        session.query(TecnologiaProyeccion).filter(TecnologiaProyeccion.id == id).delete()
    except:
        raise ValueError('Error al eliminar una Tecnologia de Proyeccion')
    finally:
        session.commit()


def get_tecnologia_proyeccion(id):    
    tecnologiaproyeccion = session.query(TecnologiaProyeccion).filter(TecnologiaProyeccion.id == id).first()
    return tecnologiaproyeccion

