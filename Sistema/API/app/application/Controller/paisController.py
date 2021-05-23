from flask import Blueprint
from flask import current_app as app
from flask import Response
from ..Logic import paisService

# Blueprint Configuration
pais_bp = Blueprint(
    'pais_bp', __name__
)


@pais_bp.route('/pais', methods=['GET'])
def pais():
    return Response('{"data": "JSON string example"}',headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")

@pais_bp.route('/pais/<nombre>', methods=['GET','POST'])
def pais_create(nombre):
    print(nombre)
    paisService.create_pais(nombre)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")