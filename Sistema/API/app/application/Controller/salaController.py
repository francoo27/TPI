from ..Model.ClasificacionModel import ClasificacionSchema
from ..Model.SalaModel import SalaSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import salaService
from marshmallow import Schema, fields, ValidationError


# Blueprint Configuration
sala_bp = Blueprint(
    'sala_bp', __name__
)
salaSchema = SalaSchema()
salasSchema = SalaSchema(many=True)

@sala_bp.route('/api/sala', methods=['GET'])
def query_sala():
    sala = salaService.query_sala()
    output = salasSchema.dump(sala)
    return jsonify(output)

@sala_bp.route('/api/sala/complejo/<complejoId>', methods=['GET'])
def query_sala_byComplejo(complejoId):
    sala = salaService.query_sala_byComplejo(complejoId)
    output = salasSchema.dump(sala)
    return jsonify(output)

