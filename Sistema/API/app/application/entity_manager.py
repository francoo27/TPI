from config import DevConfig
from .Model.PaisModel import Pais
from .Model.AudioModel import Audio
from .connection_manager import SessionManager

session = SessionManager.getInstance()


class EntityManager():
    def seed_database():
        # connection_engine.execute(f"INSERT INTO {DevConfig.DATABASE_SCHEMA}.pais (nombre) VALUES ('Argentina');")
        # Pais
        session.add(Pais(nombre = 'Argentina'))
        session.add(Pais(nombre = 'Uruguay'))
        # Pais
        # Audio
        session.add(Audio(nombre = 'Español'))
        session.add(Audio(nombre = 'Español Latino'))
        session.add(Audio(nombre = 'Ingles'))
        session.add(Audio(nombre = 'Ingles (Subtitulado)'))
        session.add(Audio(nombre = 'Frances'))
        session.add(Audio(nombre = 'Frances (Subtitulado)'))
        # Audio
        session.commit()