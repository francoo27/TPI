from ..Model.ClasificacionModel import ClasificacionSchema
from ..Model.FormatoModel import FormatoSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import formatoService
from marshmallow import Schema, fields, ValidationError
from http import HTTPStatus
import json


# Blueprint Configuration
formato_bp = Blueprint(
    'formato_bp', __name__
)
formatoSchema = FormatoSchema()
formatosSchema = FormatoSchema(many=True)


@formato_bp.route('/api/formato/<id>', methods=['GET'])
def get_formato(id):
    formato =  formatoService.get_formato(id)
    output = formatoSchema.dump(formato)
    return jsonify(output)


@formato_bp.route('/api/formato', methods=['GET'])
def query_formato():
    formato = formatoService.query_formato()
    output = formatosSchema.dump(formato)
    return jsonify(output)




@formato_bp.route('/api/formato', methods=['POST'])
def formato_create():
    if request.data:
        json_data = request.get_json()
    else:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        data = formatoSchema.load(json_data)
    except Exception as e :
        return {e: "Error"}, 422
    try:
        formatoService.formato_create(data)
    except ValueError as e :
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@formato_bp.route('/api/formato/<id>', methods=['PUT'])
def formato_update(id):
    json_data = request.get_json()
    print(json_data)
    if not json_data:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        # WORKAROUND https://www.gitmemory.com/issue/marshmallow-code/flask-marshmallow/44/508944019
        data = formatoSchema.load(json_data,session=db.session)
    except Exception as e :
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
    formatoService.formato_update(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@formato_bp.route('/api/formato/<id>', methods=['DELETE'])
def formato_delete(id):
    try:
        formatoService.formato_delete(id)
    except ValueError as e :
        print(e)
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
    return Response(headers=dict({
    "HeaderExample": "HeaderContent"
    }),mimetype="application/json")