from ..Model.AsientoModel import AsientoSchema
from ..Model.AsientoModel import AsientoSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import asientoService
from marshmallow import Schema, fields, ValidationError
from ..Logic.emailService import sendmail


# Blueprint Configuration
asiento_bp = Blueprint(
    'asiento_bp', __name__
)
asientoSchema = AsientoSchema()
asientosSchema = AsientoSchema(many=True)



@asiento_bp.route('/api/asiento/<id>', methods=['GET'])
def query_asiento(id):
    asiento = asientoService.query_ocupados_by_funcion(id)
    output = asientosSchema.dump(asiento)
    sendmail()
    return jsonify(output)

@asiento_bp.route('/api/asiento/funcion/<id>', methods=['GET'])
def query_asiento_occupied(id):
    asiento = asientoService.query_ocupados_by_funcion(id)
    output = asientosSchema.dump(asiento)
    return jsonify(output)
