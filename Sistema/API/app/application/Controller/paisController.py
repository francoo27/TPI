from .util.auth import authorize
from ..Model.PaisModel import PaisSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import paisService
from marshmallow import Schema, fields, ValidationError
from ..Shared import db


# Blueprint Configuration
pais_bp = Blueprint(
    'pais_bp', __name__
)
paisSchema = PaisSchema()
paisesSchema = PaisSchema(many=True)


@pais_bp.route('/api/pais/<id>', methods=['GET'])
@authorize
def get_pais(id):
    pais =  paisService.get_pais(id)
    output = paisSchema.dump(pais)
    return jsonify(output)


@pais_bp.route('/api/pais', methods=['GET'])
def query_pais():
    pais = paisService.query_pais()
    output = paisesSchema.dump(pais)
    return jsonify(output)


@pais_bp.route('/api/pais', methods=['POST'])
def pais_create():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    # Validate and deserialize input
    try:
        data = paisSchema.load(json_data)
    except:
        return {"message": "Error"}, 422
    paisService.pais_create(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@pais_bp.route('/api/pais/<id>', methods=['PUT'])
def pais_update(id):
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    # Validate and deserialize input
    try:
        # WORKAROUND https://www.gitmemory.com/issue/marshmallow-code/flask-marshmallow/44/508944019
        data = paisSchema.load(json_data ,session=db.session)
    except:
        return {"message": "Error"}, 422
    paisService.pais_update(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@pais_bp.route('/pais/<id>', methods=['DELETE'])
def pais_delete(id):
    paisService.pais_delete(id)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")