from .BaseModel import BaseModel
from ..Shared import db
from ..Shared import ma

class Audio(BaseModel):
    __tablename__ = 'audio'
    nombre = db.Column(db.String(128))

class AudioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Audio
        load_instance = True

