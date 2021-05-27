from .BaseModel import BaseModel
from ..Shared import db
from ..Shared import ma
from marshmallow_sqlalchemy import ModelSchema

class Pais(BaseModel):
    __tablename__ = 'pais'
    nombre = db.Column(db.String(128), nullable=False)


class PaisSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pais
        load_instance = True

