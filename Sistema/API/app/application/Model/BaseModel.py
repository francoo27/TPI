from typing import Text, TextIO
from ..Shared import db
from .Serializer import Serializer
class BaseModel(db.Model, Serializer):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_creacion = db.Column(db.DateTime, server_default=db.func.now())
    fecha_modificacion = db.Column(db.DateTime, server_default=db.func.now())