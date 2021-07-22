from ..Model.ClasificacionModel import ClasificacionSchema
from ..Model.FuncionModel import FuncionSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import funcionService
from marshmallow import Schema, fields, ValidationError
from ..Shared import db

# Blueprint Configuration
funcion_bp = Blueprint(
    'funcion_bp', __name__
)
funcionSchema = FuncionSchema()
funcionsSchema = FuncionSchema(many=True)


@funcion_bp.route('/api/funcion/<id>', methods=['GET'])
def get_funcion(id):
    funcion =  funcionService.get_funcion(id)
    output = funcionSchema.dump(funcion)
    return jsonify(output)


@funcion_bp.route('/api/funcion', methods=['GET'])
def query_funcion():
    funcion = funcionService.query_funcion()
    output = funcionsSchema.dump(funcion)
    return jsonify(output)


@funcion_bp.route('/api/funcion', methods=['POST'])
def funcion_create():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    # Validate and deserialize input
    try:
        data = funcionSchema.load(json_data)
    except:
        return {"message": "Error"}, 422
    funcionService.funcion_create(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@funcion_bp.route('/api/funcion/<id>', methods=['PUT'])
def funcion_update(id):
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    # Validate and deserialize input
    try:
        data = funcionSchema.load(json_data,session=db.session)
    except:
        return {"message": "Error"}, 422
    funcionService.funcion_update(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@funcion_bp.route('/api/funcion/<id>', methods=['DELETE'])
def funcion_delete(id):
    funcionService.funcion_delete(id)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@funcion_bp.route('/api/funcion/pelicula/<peliculaId>/formato/<formatoId>', methods=['GET'])
def query_ByPeliculaAndFormato(peliculaId,formatoId):
    funcion =  funcionService.query_ByPeliculaAndFormato(peliculaId,formatoId)
    output = funcionsSchema.dump(funcion)
    return jsonify(output)