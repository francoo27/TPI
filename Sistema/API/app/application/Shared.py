from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
r = FlaskRedis()
migrateObj = Migrate()
ma = Marshmallow()