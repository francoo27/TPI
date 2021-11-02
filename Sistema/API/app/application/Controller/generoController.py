from ..Model.GeneroModel import GeneroSchema
from ..Model.GeneroModel import GeneroSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import generoService
from marshmallow import Schema, fields, ValidationError
from ..Shared import db
from http import HTTPStatus
import json
# Blueprint Configuration
genero_bp = Blueprint(
    'genero_bp', __name__
)
generoSchema = GeneroSchema()
generosSchema = GeneroSchema(many=True)


@genero_bp.route('/api/genero/<id>', methods=['GET'])
def get_genero(id):
    genero =  generoService.get_genero(id)
    output = generoSchema.dump(genero)
    return jsonify(output)


@genero_bp.route('/api/genero', methods=['GET'])
def query_genero():
    genero = generoService.query_genero()
    output = generosSchema.dump(genero)
    return jsonify(output)

@genero_bp.route('/api/genero', methods=['POST'])
def genero_create():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    # Validate and deserialize input
    try:
        data = generoSchema.load(json_data)
    except:
        return {"message": "Error"}, 422
    generoService.genero_create(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")

@genero_bp.route('/api/genero/<id>', methods=['PUT'])
def genero_update(id):
    json_data = request.get_json()
    print(json_data)
    if not json_data:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        # WORKAROUND https://www.gitmemory.com/issue/marshmallow-code/flask-marshmallow/44/508944019
        data = generoSchema.load(json_data,session=db.session)
    except Exception as e :
        print(e)
        return {"message": "Error"}, 422
    generoService.genero_update(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")

@genero_bp.route('/api/genero/<id>', methods=['DELETE'])
def clasificacion_delete(id):
    try:
        generoService.genero_delete(id)
    except ValueError as e :
        print(e)
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
    return Response(headers=dict({
    "HeaderExample": "HeaderContent"
    }),mimetype="application/json")