from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.FuncionModel import Funcion,FuncionSchema
funcionSchema = FuncionSchema()

session = SessionManager.getInstance()
def funcion_create(funcion):
    session.add(funcion)
    session.commit()

def funcion_update(funcion):
    session.query(Funcion).filter(Funcion.id == funcion.id).update(funcionSchema.dump(funcion))
    session.commit()

def get_funcion(id):
    funcion = session.query(Funcion).filter(Funcion.id == id).first()
    return funcion

def query_funcion():
    funcion = session.query(Funcion).all()
    return funcion

def funcion_delete(id):
    session.query(Funcion).filter(Funcion.id == id).delete()
    session.commit()