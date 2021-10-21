from .BaseModel import BaseModel
from .PrecioModel import PrecioSchema
from .AsientoModel import AsientoSchema
from ..Shared import db
from ..Shared import ma

class Ticket(BaseModel):
    __tablename__ = 'ticket'

    id_asiento = db.Column(db.Integer, db.ForeignKey('asiento.id'),nullable=False)
    asiento = db.relationship("Asiento", backref=db.backref("asiento", uselist=False),lazy='subquery')
    id_precio = db.Column(db.Integer, db.ForeignKey('precio.id'),nullable=False)
    precio = db.relationship("Precio", backref=db.backref("precio", uselist=False),lazy='subquery')

class TicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket
        load_instance = True
        sqla_session = db.session

    asiento = AsientoSchema()
    precio = PrecioSchema()
