from http import HTTPStatus
import json
from ..Model.TecnologiaProyeccionModel import TecnologiaProyeccionSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import tecnologiaProyeccionService
from marshmallow import Schema, fields, ValidationError
from ..Shared import db


# Blueprint Configuration
tecnologiaProyeccion_bp = Blueprint(
    'tecnologiaProyeccion_bp', __name__
)
tecnologiaProyeccionSchema = TecnologiaProyeccionSchema()
tecnologiaProyeccionsSchema = TecnologiaProyeccionSchema(many=True)


@tecnologiaProyeccion_bp.route('/api/tecnologia-proyeccion/<id>', methods=['GET'])
def get_tecnologia_proyeccion(id):
    tecnologiaProyeccion =  tecnologiaProyeccionService.get_tecnologia_proyeccion(id)
    output = tecnologiaProyeccionSchema.dump(tecnologiaProyeccion)
    return jsonify(output)


@tecnologiaProyeccion_bp.route('/api/tecnologia-proyeccion', methods=['GET'])
def query_tecnologia_proyeccion():
    tecnologiaProyeccion = tecnologiaProyeccionService.query_tecnologia_proyeccion()
    output = tecnologiaProyeccionsSchema.dump(tecnologiaProyeccion)
    return jsonify(output)


@tecnologiaProyeccion_bp.route('/api/tecnologia-proyeccion', methods=['POST'])
def tecnologia_proyeccion_create():
    if request.data:
        json_data = request.get_json()
    else:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        data = tecnologiaProyeccionSchema.load(json_data)
    except Exception as e :
        print(e)
        return {e: "Error"}, 422
    try:
        tecnologiaProyeccionService.tecnologia_proyeccion_create(data)
    except ValueError as e :
        return {e: "Error"}, 400
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@tecnologiaProyeccion_bp.route('/api/tecnologia-proyeccion/<id>', methods=['PUT'])
def tecnologia_proyeccion_update(id):
    json_data = request.get_json()
    print(json_data)
    if not json_data:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        # WORKAROUND https://www.gitmemory.com/issue/marshmallow-code/flask-marshmallow/44/508944019
        data = tecnologiaProyeccionSchema.load(json_data,session=db.session)
    except Exception as e :
        return {"message": "Error"}, 422
    tecnologiaProyeccionService.tecnologia_proyeccion_update(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@tecnologiaProyeccion_bp.route('/api/tecnologia-proyeccion/<id>', methods=['DELETE'])
def tecnologia_proyeccion_delete(id):
    try:
        tecnologiaProyeccionService.tecnologia_proyeccion_delete(id)
    except ValueError as e :
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
    return Response(headers=dict({
    "HeaderExample": "HeaderContent"
    }),mimetype="application/json")