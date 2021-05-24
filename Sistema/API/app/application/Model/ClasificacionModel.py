
from .BaseModel import BaseModel
from ..Shared import db


class Clasificacion(BaseModel):
    __tablename__ = 'clasificacion'
    nombre: str
    nombre = db.Column(db.String(128))
