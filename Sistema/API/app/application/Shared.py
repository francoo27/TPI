from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_migrate import Migrate

db = SQLAlchemy()
r = FlaskRedis()
migrateObj = Migrate()