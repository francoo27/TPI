from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.FormatoModel import Formato,FormatoSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
formatoSchema = FormatoSchema()

engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(engine)

def get_formato(id):    
    with Session() as session:
        formato = session.query(Formato).filter(Formato.id == id).first()
    return formato

def query_formato():
    with Session() as session:
        formato = session.query(Formato).all()
    return formato