from .BaseModel import BaseModel
from .FuncionModel import FuncionSchema
from .AsientoModel import AsientoSchema
from ..Shared import db
from ..Shared import ma
import marshmallow_sqlalchemy as masqla

compraTicket = db.Table('compra_ticket', db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('id_compra', db.Integer, db.ForeignKey('compra.id')),
    db.Column('id_ticket', db.Integer, db.ForeignKey('ticket.id'))
)

class Compra(BaseModel):
    __tablename__ = 'compra'
    email = db.Column(db.String(128),nullable=False)

    id_funcion = db.Column(db.Integer, db.ForeignKey('funcion.id'),nullable=False)
    funcion = db.relationship("Funcion", backref=db.backref("funcion", uselist=False),lazy='subquery')
    # Formatos
    tickets = db.relationship("Ticket",
                    secondary=compraTicket,lazy='subquery',backref=db.backref('compra', lazy=True))
    

class CompraSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Compra
        load_instance = True
        sqla_session = db.session
    asientos = ma.Nested(AsientoSchema())
    funcion = FuncionSchema()
    tickets = masqla.fields.Nested("TicketSchema", many=True)
