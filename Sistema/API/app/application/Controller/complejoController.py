from ..Model.ClasificacionModel import ClasificacionSchema
from ..Model.ComplejoModel import ComplejoSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import complejoService
from marshmallow import Schema, fields, ValidationError


# Blueprint Configuration
complejo_bp = Blueprint(
    'complejo_bp', __name__
)
complejoSchema = ComplejoSchema()
complejosSchema = ComplejoSchema(many=True)

@complejo_bp.route('/api/complejo', methods=['GET'])
def query_complejo():
    complejo = complejoService.query_complejo()
    output = complejosSchema.dump(complejo)
    return jsonify(output)

