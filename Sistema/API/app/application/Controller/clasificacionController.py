from ..Model.ClasificacionModel import ClasificacionSchema
from ..Model.ClasificacionModel import ClasificacionSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import clasificacionService
from marshmallow import Schema, fields, ValidationError
from http import HTTPStatus
import json
from ..Shared import db

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


@clasificacion_bp.route('/api/clasificacion', methods=['POST'])
def clasificacion_create():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    # Validate and deserialize input
    try:
        data = clasificacionSchema.load(json_data)
    except:
        return {"message": "Error"}, 422
    clasificacionService.clasificacion_create(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")

@clasificacion_bp.route('/api/clasificacion/<id>', methods=['PUT'])
def clasificacion_update(id):
    json_data = request.get_json()
    print(json_data)
    if not json_data:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        # WORKAROUND https://www.gitmemory.com/issue/marshmallow-code/flask-marshmallow/44/508944019
        data = clasificacionSchema.load(json_data,session=db.session)
    except Exception as e :
        print(e)
        return {"message": "Error"}, 422
    clasificacionService.clasificacion_update(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")

@clasificacion_bp.route('/api/clasificacion/<id>', methods=['DELETE'])
def clasificacion_delete(id):
    try:
        clasificacionService.clasificacion_delete(id)
    except ValueError as e :
        print(e)
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
    return Response(headers=dict({
    "HeaderExample": "HeaderContent"
    }),mimetype="application/json")