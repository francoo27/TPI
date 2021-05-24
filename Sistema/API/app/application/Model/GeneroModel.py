from .BaseModel import BaseModel
from ..Shared import db


class Genero(BaseModel):
    __tablename__ = 'genero'
    nombre: str
    nombre = db.Column(db.String(128))

