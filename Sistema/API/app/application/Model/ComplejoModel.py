from .BaseModel import BaseModel
from .CiudadModel import CiudadSchema
from ..Shared import db
from ..Shared import ma

class Complejo(BaseModel):
    __tablename__ = 'complejo'
    nombre = db.Column(db.String(128), nullable=False)
    gerente = db.Column(db.String(128), nullable=False)
    id_ciudad = db.Column(db.Integer, db.ForeignKey('ciudad.id'), nullable=False)
    ciudad = db.relationship("Ciudad", backref=db.backref("ciudad", uselist=False))


class ComplejoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Complejo
        load_instance = True
    ciudad = ma.Nested(CiudadSchema())

