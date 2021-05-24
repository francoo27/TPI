from dataclasses import dataclass
from ..Shared import db

@dataclass
class BaseModel(db.Model):
    __abstract__ = True
    id: int
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    def __init__(self,id=None):
        id = id