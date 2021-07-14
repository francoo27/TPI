from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.FormatoModel import Formato,FormatoSchema
formatoSchema = FormatoSchema()

session = SessionManager.getInstance()
# def formato_create(formato):
#     session.add(formato)
#     session.commit()

# def formato_update(formato):
#     session.query(Formato).filter(Formato.id == formato.id).update(formatoSchema.dump(formato))
#     session.commit()

# def get_formato(id):
#     formato = session.query(Formato).filter(Formato.id == id).first()
#     return formato

def query_formato():
    formato = session.query(Formato).all()
    return formato

# def formato_delete(id):
#     session.query(Formato).filter(Formato.id == id).delete()
#     session.commit()