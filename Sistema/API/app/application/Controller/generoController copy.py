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



@compra_bp.route('/api/comprar', methods=['POST'])
def buy(id):
    try:
        generoService.genero_delete(id)
    except ValueError as e :
        print(e)
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
    return Response(headers=dict({
    "HeaderExample": "HeaderContent"
    }),mimetype="application/json")