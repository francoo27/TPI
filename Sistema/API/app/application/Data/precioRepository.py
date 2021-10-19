from sqlalchemy.sql.expression import false, text, true
from ..Model.TipoPrecioModel import TipoPrecio
from config import DevConfig
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from ..connection_manager import SessionManager
from ..Model.PrecioModel import Precio,PrecioSchema
from config import DevConfig
from ..Shared import db

# session = SessionManager.getInstance()


engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
Session = sessionmaker(engine)
session = db.session
def query_precio():
    precio = session.query(Precio).filter(Precio.activo == True).all()
    return precio

def add_precio():
    precio = session.query(Precio).filter(Precio.activo == True).all()
    return precio

def precio_create():
        precio =  session.query(Precio).first()
        tipo = session.query(TipoPrecio).filter(TipoPrecio.id == precio.tipoPrecio.id).first()
        session.query(Precio).filter(Precio.tipoPrecio == precio.tipoPrecio and Precio.activo == True).update(dict(activo=False))
        session.add(Precio(nombre="A",codigo="A",valor=333,id_tipoPrecio=tipo.id,activo=True))
        session.add(precio)
        session.commit()

def pais_update(pais):
    session.query(Precio).filter(Precio.id == pais.id).update(Precio.activo)
    session.commit()