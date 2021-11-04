from typing import final
from sqlalchemy.orm import session
from ..Model.CompraModel import Compra
from ..connection_manager import SessionManager
from ..Model.PeliculaModel import Pelicula,PeliculaSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
from ..Shared import db
peliculaSchema = PeliculaSchema()

# session = SessionManager.getInstance()
engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
Session = sessionmaker(engine)
session = db.session
def compra(email,funcionId,tickets):
    query = """INSERT INTO `car_db`.`compra`
        (`fecha_creacion`,`fecha_modificacion`,`email`,`id_funcion`)
        VALUES(CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'{email}',{funcionId})
        """.format(email=email, funcionId=funcionId)
    session.execute(query)
    compra = session.query(Compra).order_by(Compra.fecha_creacion.desc()).filter(~Compra.tickets.any()).filter(Compra.email == email).filter(Compra.id_funcion == funcionId).first()
    for t in tickets:
        session.execute( """INSERT INTO `car_db`.`compra_ticket`
        (`id_compra`,`id_ticket`)
        VALUES({idCompra},{idTicket})
        """.format(idCompra=compra.id, idTicket=t.id))
    session.commit()
    session.flush()
    session.expire(compra)
    session.refresh(compra) 
    session.expire_all()

    # compraId = session.query(Compra).order_by(Compra.fecha_creacion.desc()).filter(~Compra.tickets.any()).filter(Compra.email == email).filter(Compra.id_funcion == funcionId).first().id
    # session.query(Compra).filter(Compra.id == compraId).update(tickets= tickets)

