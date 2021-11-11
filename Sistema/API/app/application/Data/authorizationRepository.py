from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.UsuarioModel import Usuario,UsuarioSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
from ..Shared import db
import uuid
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

def login(email,password):
    usuario = session.query(Usuario).filter(Usuario.email == email and Usuario.password == password).first()
    token = None
    if usuario is not None:
        usuario.token = str(uuid.uuid4())
        session.add(usuario)
        session.commit()
        token = usuario.token
    return token

def auth(token):
    usuario = session.query(Usuario).filter(Usuario.token == token).first()
    return usuario