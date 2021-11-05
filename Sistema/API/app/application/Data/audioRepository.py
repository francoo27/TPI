from typing import final
from sqlalchemy.orm import session
from ..connection_manager import SessionManager
from ..Model.AudioModel import Audio,AudioSchema
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import session, sessionmaker
from config import DevConfig
from ..Shared import db
audioSchema = AudioSchema()

# session = SessionManager.getInstance()
engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI, echo=True)

# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
Session = sessionmaker(engine)
session = db.session
def audio_create(audio):
        session.add(audio)
        session.commit()

def audio_update(audio):
    currentAudio = session.query(Audio).filter(Audio.id == audio.id).first()
    currentAudio.nombre = audio.nombre
    session.add(currentAudio)
    session.commit()

def query_audio():
    audio = session.query(Audio).all()
    return audio

def audio_delete(id):
    audio = session.query(Audio).filter(Audio.id == id).first()
    audio.formatos = []
    try:
        session.query(Audio).filter(Audio.id == id).delete()
    except:
        raise ValueError('Error al eliminar una audio')
    finally:
        session.commit()


def get_audio(id):    
    audio = session.query(Audio).filter(Audio.id == id).first()
    return audio

