from ..Model.PrecioModel import PrecioSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import precioService
from marshmallow import Schema, fields, ValidationError


# Blueprint Configuration
precio_bp = Blueprint(
    'precio_bp', __name__
)
precioSchema = PrecioSchema()
preciosSchema = PrecioSchema(many=True)

@precio_bp.route('/api/precio', methods=['GET'])
def query_precio():
    precio = precioService.query_precio()
    output = preciosSchema.dump(precio)
    return jsonify(output)

