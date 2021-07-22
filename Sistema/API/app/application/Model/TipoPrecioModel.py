from .BaseModel import BaseModel
from ..Shared import db
from ..Shared import ma

class TipoPrecio(BaseModel):
    __tablename__ = 'tipo_precio'
    nombre = db.Column(db.String(128), nullable=False)
    codigo = db.Column(db.String(128), nullable=False)

class TipoPrecioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TipoPrecio
        load_instance = True
        sqla_session = db.session

