from dataclasses import dataclass
from .BaseModel import BaseModel
from ..Shared import db

@dataclass
class Pais(BaseModel):
    nombre: str
    nombre = db.Column(db.String(128))
    def __init__(self,nombre,id=None):
        print("init",nombre)
        nombre = nombre
        super().__init__(id)

