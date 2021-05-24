from .BaseModel import BaseModel
from ..Shared import db


class TecnologiaProyeccion(BaseModel):
    __tablename__ = 'tecnologia_proyeccion'
    nombre: str
    nombre = db.Column(db.String(128))

