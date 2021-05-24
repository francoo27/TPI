

from flask_migrate import init, upgrade, migrate
from sqlalchemy_utils import database_exists,create_database
from .connection_manager import engine as connection_engine
from config import DevConfig
from datetime import datetime
from . import alert_manager as am
from .entity_manager import EntityManager
import os
class MigrationManager():
    def validate_database():
        engine = connection_engine
        newDataBase = False
        from .Model import PaisModel ,AudioModel, ClasificacionModel, GeneroModel, TecnologiaProyeccionModel #Register all database models
        if not database_exists(engine.url): # Checks for the first time  
            create_database(engine.url)     # Create new DB
            am.alert_ok(f'New Schema {DevConfig.DATABASE_SCHEMA} Created')
            newDataBase = True
        if not os.path.isdir('./migrations'):
            init(directory='migrations', multidb=False)
            am.alert_ok(f"Migrations folder created")
        migrate(directory='migrations', message=f'{datetime.now().strftime("%d_%m_%y_%H:%M:%S")}', sql=False, head='head', splice=False, branch_label=None, version_path=None, rev_id=None)
        upgrade(directory='migrations', revision='head', sql=False, tag=None)
        if newDataBase:
            EntityManager.seed_database()