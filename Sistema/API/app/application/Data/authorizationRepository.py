from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.UsuarioModel import Usuario,UsuarioSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
from ..Shared import db
usuarioSchema = UsuarioSchema()

engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

session = db.session

def register(usuario):
    session.add(usuario)
    session.commit()

def get_usuario(id):    
    usuario = session.query(Usuario).filter(Usuario.id == id).first()
    return usuario

def get_usuario_byName(nombre):
    usuario = session.query(Usuario).filter(Usuario.nombre == nombre).first()
    return usuario
