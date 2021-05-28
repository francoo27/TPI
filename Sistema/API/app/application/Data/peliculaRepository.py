from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.PeliculaModel import Pelicula,PeliculaSchema
peliculaSchema = PeliculaSchema()

session = SessionManager.getInstance()
def pelicula_create(pelicula):
    session.add(pelicula)
    session.commit()

def pelicula_update(pelicula):
    session.query(Pelicula).filter(Pelicula.id == pelicula.id).update(peliculaSchema.dump(pelicula))
    session.commit()

def get_pelicula(id):
    pelicula = session.query(Pelicula).filter(Pelicula.id == id).first()
    return pelicula

def query_pelicula():
    pelicula = session.query(Pelicula).all()
    print(pelicula[0].clasificacion)
    return pelicula

def pelicula_delete(id):
    session.query(Pelicula).filter(Pelicula.id == id).delete()
    session.commit()