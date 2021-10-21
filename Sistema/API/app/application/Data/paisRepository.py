from re import A
from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.PaisModel import Pais,PaisSchema
from ..Model.CompraModel import Compra
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
    compra = session.query(Compra).filter(Compra.id_funcion == 2)
    e = 3
    if e is not None:
        compra.filter(Compra.id_funcion == e).all()
    asientos = []
    if compra is not None:
        for compra in compra:
            for ticket in compra.tickets:
                asientos.append(ticket)
                print(asientos)           
    return pais

def pais_delete(id):
    session.query(Pais).filter(Pais.id == id).delete()
    session.commit()