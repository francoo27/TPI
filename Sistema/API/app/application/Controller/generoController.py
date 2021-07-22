from ..Model.GeneroModel import GeneroSchema
from ..Model.GeneroModel import GeneroSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import generoService
from marshmallow import Schema, fields, ValidationError


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
