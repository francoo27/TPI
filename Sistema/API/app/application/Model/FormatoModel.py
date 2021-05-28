from .BaseModel import BaseModel
from .AudioModel import Audio
from .TecnologiaProyeccionModel import TecnologiaProyeccion
from ..Shared import db
from ..Shared import ma

class Formato(BaseModel):
    __tablename__ = 'formato'
    nombre = db.Column(db.String(128), nullable=False)
    id_audio = db.Column(db.Integer, db.ForeignKey('audio.id'))
    audio = db.relationship("Audio", backref=db.backref("audio", uselist=False))
    id_tecnologia_proyeccion = db.Column(db.Integer, db.ForeignKey('tecnologia_proyeccion.id'))
    tecnologiaProyeccion = db.relationship("TecnologiaProyeccion", backref=db.backref("tecnologia_proyeccion", uselist=False))

class FormatoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Formato
        load_instance = True
