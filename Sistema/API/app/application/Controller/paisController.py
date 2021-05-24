from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import paisService
import json
from types import SimpleNamespace

# Parse JSON into an object with attributes corresponding to dict keys.

# Blueprint Configuration
pais_bp = Blueprint(
    'pais_bp', __name__
)


@pais_bp.route('/pais/<id>', methods=['GET'])
def get_pais(id):
    pais = paisService.get_pais(id)
    return jsonify(pais)

@pais_bp.route('/pais', methods=['GET'])
def query_pais():
    pais = paisService.query_pais()
    return jsonify(pais)
    # Response( body,headers=dict({
    #                 "HeaderExample": "HeaderContent"
    #               }),mimetype="application/json")

@pais_bp.route('/pais', methods=['POST'])
def pais_create():
    print(str(request.data))
    pais = json.loads(request.data, object_hook=lambda d: SimpleNamespace(**d))
    paisService.pais_create(pais.nombre)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")

@pais_bp.route('/pais/<id>', methods=['PUT'])
def pais_update(id):
    print(str(request.data))
    pais = json.loads(request.data, object_hook=lambda d: SimpleNamespace(**d))
    paisService.pais_update(id,pais.nombre)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")

@pais_bp.route('/pais/<id>', methods=['DELETE'])
def pais_delete(id):
    paisService.pais_delete(id)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")