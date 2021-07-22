from .BaseModel import BaseModel
from ..Shared import db
from ..Shared import ma

class Precio(BaseModel):
    __tablename__ = 'precio'
    nombre = db.Column(db.String(128), nullable=False)
    codigo = db.Column(db.String(128), nullable=False)
    valor = db.Column(db.Numeric(), nullable=False)

class PrecioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Precio
        load_instance = True
        sqla_session = db.session

