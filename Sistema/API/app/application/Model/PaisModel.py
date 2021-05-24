from .BaseModel import BaseModel
from ..Shared import db


class Pais(BaseModel):
    __tablename__ = 'pais'
    nombre = db.Column(db.String(128), nullable=False)