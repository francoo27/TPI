from .BaseModel import BaseModel
from ..Shared import db
from ..Shared import ma

class Genero(BaseModel):
    __tablename__ = 'genero'
    nombre = db.Column(db.String(128))


class GeneroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genero
        load_instance = True
