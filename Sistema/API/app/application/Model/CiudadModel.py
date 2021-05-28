from .BaseModel import BaseModel
from .PaisModel import PaisSchema
from ..Shared import db
from ..Shared import ma

class Ciudad(BaseModel):
    __tablename__ = 'ciudad'
    nombre = db.Column(db.String(128), nullable=False)
    id_pais = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    pais = db.relationship("Pais", backref=db.backref("pais_ciudad", uselist=False))


class CiudadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ciudad
        load_instance = True
    pais = ma.Nested(PaisSchema())

