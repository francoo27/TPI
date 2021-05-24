from .BaseModel import BaseModel
from ..Shared import db


class Audio(BaseModel):
    __tablename__ = 'audio'
    nombre: str
    nombre = db.Column(db.String(128))

