from config import DevConfig
from .Model.PaisModel import Pais
from .connection_manager import SessionManager

session = SessionManager.getInstance()


class EntityManager():
    def seed_database():
        # connection_engine.execute(f"INSERT INTO {DevConfig.DATABASE_SCHEMA}.pais (nombre) VALUES ('Argentina');")
        session.add(Pais(nombre = 'Argentina'))
        session.commit()