from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.PaisModel import Pais

session = SessionManager.getInstance()
def create_pais(nombre):
    print('pais data layer accesed')
    pais = Pais(nombre=nombre)
    session.add(pais)
    session.commit()

