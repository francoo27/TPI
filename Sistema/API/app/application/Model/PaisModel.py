from .BaseModel import BaseModel
from ..Shared import db
class Pais(BaseModel):
    nombre = db.Column(db.String(128))