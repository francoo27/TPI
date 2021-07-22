from ..Model.ClasificacionModel import ClasificacionSchema
from ..Model.FormatoModel import FormatoSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import formatoService
from marshmallow import Schema, fields, ValidationError


# Blueprint Configuration
formato_bp = Blueprint(
    'formato_bp', __name__
)
formatoSchema = FormatoSchema()
formatosSchema = FormatoSchema(many=True)


# @formato_bp.route('/api/formato/<id>', methods=['GET'])
# def get_formato(id):
#     formato =  formatoService.get_formato(id)
#     output = formatoSchema.dump(formato)
#     return jsonify(output)


@formato_bp.route('/api/formato', methods=['GET'])
def query_formato():
    formato = formatoService.query_formato()
    output = formatosSchema.dump(formato)
    return jsonify(output)


# @formato_bp.route('/api/formato', methods=['POST'])
# def formato_create():
#     json_data = request.get_json()
#     if not json_data:
#         return {"message": "No input data provided"}, 400
#     # Validate and deserialize input
#     try:
#         data = formatoSchema.load(json_data)
#     except:
#         return {"message": "Error"}, 422
#     formatoService.formato_create(data)
#     return Response(headers=dict({
#   "HeaderExample": "HeaderContent"
# }),mimetype="application/json")


# @formato_bp.route('/api/formato/<id>', methods=['PUT'])
# def formato_update(id):
#     json_data = request.get_json()
#     if not json_data:
#         return {"message": "No input data provided"}, 400
#     # Validate and deserialize input
#     try:
#         data = formatoSchema.load(json_data)
#         data.id = id
#     except:
#         return {"message": "Error"}, 422
#     formatoService.formato_update(data)
#     return Response(headers=dict({
#   "HeaderExample": "HeaderContent"
# }),mimetype="application/json")


# @formato_bp.route('/api/formato/<id>', methods=['DELETE'])
# def formato_delete(id):
#     formatoService.formato_delete(id)
#     return Response(headers=dict({
#   "HeaderExample": "HeaderContent"
# }),mimetype="application/json")