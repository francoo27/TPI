
from .BaseModel import BaseModel
from ..Shared import db
from ..Shared import ma

class Clasificacion(BaseModel):
    __tablename__ = 'clasificacion'
    identificador = db.Column(db.String(128))
    edadMinima = db.Column('edad_minima',db.String(128))
    recomendacion = db.Column(db.String(128))
    definicion = db.Column(db.String(500))

class ClasificacionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Clasificacion
        load_instance = True