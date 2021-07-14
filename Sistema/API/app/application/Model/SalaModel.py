from .BaseModel import BaseModel
from .FormatoModel import FormatoSchema
from .ComplejoModel import ComplejoSchema
from ..Shared import db
from ..Shared import ma


salaFormato = db.Table('sala_formato', db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('id_sala', db.Integer, db.ForeignKey('sala.id')),
    db.Column('id_formato', db.Integer, db.ForeignKey('formato.id'))
)

class Sala(BaseModel):
    __tablename__ = 'sala'
    numero = db.Column(db.Integer(), nullable=False)
    id_complejo = db.Column(db.Integer, db.ForeignKey('complejo.id'), nullable=False)
    complejo = db.relationship("Complejo", backref=db.backref("complejo", uselist=False),lazy='subquery')
    formatos = db.relationship("Formato",
                    secondary=salaFormato,lazy='subquery')

class SalaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sala
        load_instance = True
    formatos = ma.Nested(FormatoSchema(), many = True)
    complejo = ma.Nested(ComplejoSchema())
    

