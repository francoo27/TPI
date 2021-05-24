from ..Shared import db
from .Serializer import Serializer
class BaseModel(db.Model, Serializer):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)