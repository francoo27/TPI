from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.PeliculaModel import Pelicula,PeliculaSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
peliculaSchema = PeliculaSchema()

# session = SessionManager.getInstance()
engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
Session = sessionmaker(engine)
def pelicula_create(pelicula):
    session.add(pelicula)
    session.commit()

def pelicula_update(pelicula):
    session.query(Pelicula).filter(Pelicula.id == pelicula.id).update(peliculaSchema.dump(pelicula))
    session.commit()

def get_pelicula(id):    
    with Session() as session:
        pelicula = session.query(Pelicula).filter(Pelicula.id == id).first()
    return pelicula

def query_pelicula():
    with Session() as session:
        pelicula = session.query(Pelicula).all()
    return pelicula

def pelicula_delete(id):
    session.query(Pelicula).filter(Pelicula.id == id).delete()
    session.commit()