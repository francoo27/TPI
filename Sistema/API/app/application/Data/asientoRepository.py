from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.CompraModel import Compra

session = SessionManager.getInstance()

def query_ocupados_by_funcion(id):
    compra = session.query(Compra).filter(Compra.id_funcion == id).all()
    asientos = []
    if compra is not None:
        for compra in compra:
            for ticket in compra.tickets:
                asientos.append(ticket.asiento)
                print(asientos)
    return asientos
