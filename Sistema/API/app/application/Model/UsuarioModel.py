from .BaseModel import BaseModel
from ..Shared import db
from ..Shared import ma

class Usuario(BaseModel):
    __tablename__ = 'usuario'
    public_id = db.Column(db.String(256))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    password = db.Column(db.String(256))
    admin = db.Column(db.Boolean)
    gerente = db.Column(db.Boolean)
    email = db.Column(db.String(256))

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
        sqla_session = db.session

