from config import DevConfig
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from ..connection_manager import SessionManager
from ..Model.FuncionModel import Funcion,FuncionSchema
from config import DevConfig
from ..Shared import db
from datetime import date,datetime
funcionSchema = FuncionSchema()

# session = SessionManager.getInstance()


engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
Session = sessionmaker(engine)
session = db.session
def funcion_create(funcion):
    query = """INSERT INTO `car_db`.`funcion`
        (`fecha_creacion`,`fecha_modificacion`,`nombre`,`fechaInicio`,`horaInicio`,`id_pelicula`,`id_formato`,`id_sala`)
        VALUES(CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'{nombre}','{fechaInicio}','{horaInicio}',{peliculaId},{formatoId},{salaId})
        """.format(nombre=funcion['nombre'], fechaInicio=f"{funcion['fechaAnio']}-{funcion['fechaMes']}-{funcion['fechaDia']}", horaInicio=f"{funcion['hora']}:{funcion['minuto']}:00", peliculaId=funcion['peliculaId'], formatoId=funcion['formatoId'], salaId=funcion['salaId'])
    session.execute(query)
    session.commit()

def funcion_update(funcion):
    currentFuncion = session.query(Funcion).filter(Funcion.id == funcion.id).first()
    currentFuncion.codigo = funcion.codigo
    currentFuncion.nombre = funcion.nombre
    currentFuncion.pelicula = funcion.pelicula
    currentFuncion.formato = funcion.formato
    session.add(currentFuncion)
    session.commit()

def get_funcion(id):
    funcion = session.query(Funcion).filter(Funcion.id == id).first()
    return funcion


def query_funcion():
    funcion = session.query(Funcion).all()
    return funcion


def query_ByPeliculaAndFormato(peliculaId,fomatoId):
    funcion = session.query(Funcion).filter(Funcion.id_pelicula == peliculaId and Funcion.id_formato == fomatoId ).filter(Funcion.horaInicio > datetime.now().time()).all()
    return funcion

def funcion_delete(id):
    session.query(Funcion).filter(Funcion.id == id).delete()
    session.commit()

def funcion_can_create(fechaInicio, horaInicio):
    return session.query(Funcion).filter(Funcion.fechaInicio == fechaInicio and Funcion.horaInicio == horaInicio).count() > 0

# def qq():
#     funcion = session.query(Funcion).filter(Funcion.id == id and Funcion.id).all()
#     return funcion
