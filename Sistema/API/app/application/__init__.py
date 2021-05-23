from flask import Flask
from sqlalchemy.sql.sqltypes import DateTime
from flask_migrate import Migrate, init, upgrade, migrate
from sqlalchemy_utils import database_exists,create_database
from sqlalchemy.sql import table, column
from .connection_manager import engine as connection_engine
from .entity_manager import EntityManager
from .migration_manager import MigrationManager
from config import DevConfig
from datetime import datetime
import os
from . import alert_manager as am
from .Shared import db ,r ,migrateObj


# Globally accessible libraries



def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    migrateObj.init_app(app, db)


    with app.app_context():
        # Include our Routes
        from .Controller import homeController, paisController
        MigrationManager.validate_database()
        # Register Blueprints
        app.register_blueprint(homeController.home_bp)
        app.register_blueprint(paisController.pais_bp)

        return app


# def validate_database():
#     engine = connection_engine
#     newDataBase = False
#     from .Model import PaisModel #Register all database models
#     if not database_exists(engine.url): # Checks for the first time  
#         create_database(engine.url)     # Create new DB
#         am.alert_ok(f'New Schema {DevConfig.DATABASE_SCHEMA} Created')
#         newDataBase = True
#     if not os.path.isdir('./migrations'):
#         init(directory='migrations', multidb=False)
#         am.alert_ok(f"Migrations folder created")
#     migrate(directory='migrations', message=f'{datetime.now().strftime("%d_%m_%y_%H:%M:%S")}', sql=False, head='head', splice=False, branch_label=None, version_path=None, rev_id=None)
#     upgrade(directory='migrations', revision='head', sql=False, tag=None)
#     if newDataBase:
#         EntityManager.seed_database()
