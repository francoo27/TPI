from .BaseModel import BaseModel
from ..Shared import db
from ..Shared import ma

class Asiento(BaseModel):
    __tablename__ = 'asiento'
    nombre = db.Column(db.String(128), nullable=True)
    fila = db.Column(db.Integer(), nullable=True)
    columna = db.Column(db.Integer(), nullable=True)
    numero = db.Column(db.Integer(), nullable=True)
    adaptado = db.Column(db.Boolean(), nullable=True)

class AsientoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Asiento
        load_instance = True
        sqla_session = db.session

