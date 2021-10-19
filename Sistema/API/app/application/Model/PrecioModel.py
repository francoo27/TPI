from .BaseModel import BaseModel
from .TipoPrecioModel import TipoPrecioSchema
from ..Shared import db
from ..Shared import ma

class Precio(BaseModel):
    __tablename__ = 'precio'
    nombre = db.Column(db.String(128), nullable=False)
    codigo = db.Column(db.String(128), nullable=False)
    valor = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None), nullable=False)
    activo = db.Column(db.Boolean(), nullable=False)
    # Precio
    id_tipoPrecio = db.Column(db.Integer, db.ForeignKey('tipo_precio.id'))
    tipoPrecio = db.relationship("TipoPrecio", backref=db.backref("tipo_precio", uselist=False),lazy='subquery')

class PrecioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Precio
        load_instance = True
        sqla_session = db.session
    tipoPrecio = ma.Nested(TipoPrecioSchema())
