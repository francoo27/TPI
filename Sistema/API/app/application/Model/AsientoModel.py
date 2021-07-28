from .BaseModel import BaseModel
from ..Shared import db
from ..Shared import ma

class Asiento(BaseModel):
    __tablename__ = 'asiento'
    nombre = db.Column(db.String(128), nullable=False)
    fila = db.Column(db.Integer(), nullable=False)
    columna = db.Column(db.Integer(), nullable=False)
    adaptado = db.Column(db.Boolean(), nullable=False)

class AsientoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Asiento
        load_instance = True
        sqla_session = db.session

