from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.PaisModel import Pais

session = SessionManager.getInstance()
def pais_create(nombre):
    pais = Pais(nombre,None)
    pais.nombre = nombre
    session.add(pais)
    session.commit()

def pais_update(id, nombre):
    session.query(Pais).filter(Pais.id == id).update({"nombre": nombre})
    session.commit()

def get_pais(id):
    pais = session.query(Pais).filter(Pais.id == id)
    return pais

def query_pais():
    pais = session.query(Pais).all()
    return pais

def pais_delete(id):
    session.query(Pais).filter(Pais.id == id).delete()
    session.commit()