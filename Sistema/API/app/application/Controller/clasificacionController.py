from ..Model.ClasificacionModel import ClasificacionSchema
from ..Model.ClasificacionModel import ClasificacionSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import clasificacionService
from marshmallow import Schema, fields, ValidationError


# Blueprint Configuration
clasificacion_bp = Blueprint(
    'clasificacion_bp', __name__
)
clasificacionSchema = ClasificacionSchema()
clasificacionsSchema = ClasificacionSchema(many=True)


@clasificacion_bp.route('/api/clasificacion/<id>', methods=['GET'])
def get_clasificacion(id):
    clasificacion =  clasificacionService.get_clasificacion(id)
    output = clasificacionSchema.dump(clasificacion)
    return jsonify(output)


@clasificacion_bp.route('/api/clasificacion', methods=['GET'])
def query_clasificacion():
    clasificacion = clasificacionService.query_clasificacion()
    output = clasificacionsSchema.dump(clasificacion)
    return jsonify(output)
