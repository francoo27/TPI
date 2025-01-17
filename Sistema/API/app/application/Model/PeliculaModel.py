from sqlalchemy.orm import backref
from .BaseModel import BaseModel
from .ClasificacionModel import ClasificacionSchema
from .PaisModel import PaisSchema
from .FormatoModel import FormatoSchema
from .GeneroModel import GeneroSchema
from ..Shared import db
from ..Shared import ma
import marshmallow_sqlalchemy as masqla

peliculaFormato = db.Table('pelicula_formato', db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('id_pelicula', db.Integer, db.ForeignKey('pelicula.id')),
    db.Column('id_formato', db.Integer, db.ForeignKey('formato.id'))
)

class Pelicula(BaseModel):
    __tablename__ = 'pelicula'
    tituloOriginal = db.Column('titulo_original',db.String(128), nullable=False)
    tituloPais = db.Column('titulo_pais',db.String(128), nullable=False)
    fechaEstreno = db.Column('fecha_estreno',db.String(128), nullable=True)
    imagen = db.Column('imagen',db.String(300))
    duracion = db.Column('duracion',db.Integer())
    sinopsis = db.Column('sinopsis',db.String(500))
    # Clasifiacion
    id_clasificacion = db.Column(db.Integer, db.ForeignKey('clasificacion.id'))
    clasificacion = db.relationship("Clasificacion", backref=db.backref("clasificacion", uselist=False),lazy='subquery')
    # Pais
    id_pais = db.Column(db.Integer, db.ForeignKey('pais.id'))
    pais = db.relationship("Pais", backref=db.backref("pais_pelicula", uselist=False),lazy='subquery')
    # Genero
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id'))
    genero = db.relationship("Genero", backref=db.backref("genero", uselist=False),lazy='subquery')
    # Formatos
    formatos = db.relationship("Formato",
                    secondary=peliculaFormato,lazy='subquery',backref=db.backref('pelicula', lazy=True))


class PeliculaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pelicula
        load_instance = True
        sqla_session = db.session
    clasificacion = ma.Nested(ClasificacionSchema())
    pais = ma.Nested(PaisSchema())
    genero = ma.Nested(GeneroSchema())
    formatos = masqla.fields.Nested("FormatoSchema", many=True)


