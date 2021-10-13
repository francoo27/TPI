from http import HTTPStatus
import json
from ..Model.FormatoModel import FormatoSchema
from ..Model.ClasificacionModel import ClasificacionSchema
from ..Model.PeliculaModel import PeliculaSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import peliculaService
from marshmallow import Schema, fields, ValidationError
from ..Shared import db


# Blueprint Configuration
pelicula_bp = Blueprint(
    'pelicula_bp', __name__
)
peliculaSchema = PeliculaSchema()
peliculasSchema = PeliculaSchema(many=True)

formatosSchema = FormatoSchema(many=True)


@pelicula_bp.route('/api/pelicula/<id>', methods=['GET'])
def get_pelicula(id):
    pelicula =  peliculaService.get_pelicula(id)
    output = peliculaSchema.dump(pelicula)
    return jsonify(output)


@pelicula_bp.route('/api/pelicula', methods=['GET'])
def query_pelicula():
    pelicula = peliculaService.query_pelicula()
    output = peliculasSchema.dump(pelicula)
    return jsonify(output)


@pelicula_bp.route('/api/pelicula', methods=['POST'])
def pelicula_create():
    if request.data:
        json_data = request.get_json()
    else:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        data = peliculaSchema.load(json_data)
    except Exception as e :
        print(e)
        return {e: "Error"}, 422
    try:
        peliculaService.pelicula_create(data)
    except ValueError as e :
        return {e: "Error"}, 400
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@pelicula_bp.route('/api/pelicula/<id>', methods=['PUT'])
def pelicula_update(id):
    json_data = request.get_json()
    print(json_data)
    if not json_data:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        # WORKAROUND https://www.gitmemory.com/issue/marshmallow-code/flask-marshmallow/44/508944019
        data = peliculaSchema.load(json_data,session=db.session)
    except Exception as e :
        print(e)
        return {"message": "Error"}, 422
    peliculaService.pelicula_update(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@pelicula_bp.route('/api/pelicula/<id>', methods=['DELETE'])
def pelicula_delete(id):
    try:
        peliculaService.pelicula_delete(id)
    except ValueError as e :
        print(e)
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
    return Response(headers=dict({
    "HeaderExample": "HeaderContent"
    }),mimetype="application/json")