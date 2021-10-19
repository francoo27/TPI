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
from .Shared import db ,r ,migrateObj,ma


# Globally accessible libraries



def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    migrateObj.init_app(app, db)
    ma.init_app(app)


    with app.app_context():
        # Include our Routes
        from .Controller import homeController, paisController, peliculaController, funcionController
        from .Controller import formatoController, clasificacionController, generoController, imagenController 
        from .Controller import salaController, complejoController, authorizationController, precioController
        MigrationManager.validate_database()
        # Register Blueprints
        app.register_blueprint(homeController.home_bp)
        app.register_blueprint(paisController.pais_bp)
        app.register_blueprint(peliculaController.pelicula_bp)
        app.register_blueprint(funcionController.funcion_bp)
        app.register_blueprint(formatoController.formato_bp)
        app.register_blueprint(clasificacionController.clasificacion_bp)
        app.register_blueprint(generoController.genero_bp)
        app.register_blueprint(imagenController.image_bp)
        app.register_blueprint(salaController.sala_bp)
        app.register_blueprint(complejoController.complejo_bp)
        app.register_blueprint(authorizationController.authorization_bp)
        app.register_blueprint(precioController.precio_bp)
        return app

