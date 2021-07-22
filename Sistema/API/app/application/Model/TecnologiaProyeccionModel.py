from .BaseModel import BaseModel
from ..Shared import db
from ..Shared import ma

class TecnologiaProyeccion(BaseModel):
    __tablename__ = 'tecnologia_proyeccion'
    nombre = db.Column(db.String(128))

class TecnologiaProyeccionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TecnologiaProyeccion
        load_instance = True
        sqla_session = db.session