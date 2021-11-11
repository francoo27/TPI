from .BaseModel import BaseModel
from .FormatoModel import FormatoSchema
from .PeliculaModel import PeliculaSchema
from .SalaModel import SalaSchema
from ..Shared import db
from ..Shared import ma

class Funcion(BaseModel):
    __tablename__ = 'funcion'
    nombre = db.Column(db.String(128))
    fechaInicio = db.Column(db.Date(), nullable=True)
    horaInicio = db.Column(db.Time(), nullable=True)
    cancelada = db.Column(db.Boolean(), nullable=True)
    id_pelicula = db.Column(db.Integer, db.ForeignKey('pelicula.id'),nullable=False)
    pelicula = db.relationship("Pelicula", backref=db.backref("pelicula", uselist=False),lazy='subquery')

    id_formato = db.Column(db.Integer, db.ForeignKey('formato.id'),nullable=False)
    formato = db.relationship("Formato", backref=db.backref("formato", uselist=False),lazy='subquery')

    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id'),nullable=False)
    sala = db.relationship("Sala", backref=db.backref("sala", uselist=False),lazy='subquery')

class FuncionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Funcion
        load_instance = True
        sqla_session = db.session
    pelicula = ma.Nested(PeliculaSchema())
    formato = ma.Nested(FormatoSchema())
    sala = ma.Nested(SalaSchema())
