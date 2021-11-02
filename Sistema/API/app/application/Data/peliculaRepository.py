from typing import final
from sqlalchemy.orm import session
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
def pelicula_create(pelicula):
        session.add(pelicula)
        session.commit()

def pelicula_update(pelicula):
    currentPelicula = session.query(Pelicula).filter(Pelicula.id == pelicula.id).first()
    currentPelicula.formatos = pelicula.formatos
    currentPelicula.fechaEstreno = pelicula.fechaEstreno
    currentPelicula.duracion = pelicula.duracion
    currentPelicula.sinopsis = pelicula.sinopsis
    currentPelicula.clasificacion = pelicula.clasificacion
    currentPelicula.pais = pelicula.pais
    currentPelicula.tituloOriginal = pelicula.tituloOriginal
    currentPelicula.tituloPais = pelicula.tituloPais
    print("pelicula imagen",pelicula.imagen)
    currentPelicula.imagen = None if pelicula.imagen == None else pelicula.imagen
    session.add(currentPelicula)
    session.commit()

def query_pelicula():
    pelicula = session.query(Pelicula).all()
    return pelicula

def pelicula_delete(id):
    pelicula = session.query(Pelicula).filter(Pelicula.id == id).first()
    pelicula.formatos = []
    try:
        session.query(Pelicula).filter(Pelicula.id == id).delete()
    except:
        raise ValueError('Error al eliminar una pelicula')
    finally:
        session.commit()


def get_pelicula(id):    
    pelicula = session.query(Pelicula).filter(Pelicula.id == id).first()
    return pelicula


def any_pelicula_has_genero(generoId):
    return session.query(Pelicula).filter(Pelicula.id_genero == generoId).first() is not None

def any_pelicula_has_clasificacion(clasificacionId):
    return session.query(Pelicula).filter(Pelicula.id_clasificacion == clasificacionId).first() is not None
  

# session = db.session
# Session = sessionmaker(engine)
# def pelicula_create(pelicula):
#     session.add(pelicula)
#     session.commit()

# def pelicula_update(pelicula):
#     session.query(Pelicula).filter(Pelicula.id == pelicula.id).update(peliculaSchema.dump(pelicula))

