from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.PaisModel import Pais,PaisSchema
paisSchema = PaisSchema()

session = SessionManager.getInstance()
def pais_create(pais):
    print(pais)
    session.add(pais)
    session.commit()

def pais_update(pais):
    session.query(Pais).filter(Pais.id == pais.id).update(paisSchema.dump(pais))
    session.commit()

def get_pais(id):
    pais = session.query(Pais).filter(Pais.id == id).first()
    return pais

def query_pais():
    pais = session.query(Pais).all()
    return pais

def pais_delete(id):
    session.query(Pais).filter(Pais.id == id).delete()
    session.commit()