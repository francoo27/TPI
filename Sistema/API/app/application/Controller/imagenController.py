from ..Model.ClasificacionModel import ClasificacionSchema
from ..Model.PeliculaModel import PeliculaSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import peliculaService
from marshmallow import Schema, fields, ValidationError
from ..Shared import db
import base64
import json
import os
from flask import send_file,send_from_directory
from config import basedir
from pathlib import Path


# Blueprint Configuration
image_bp = Blueprint(
    'image_bp', __name__
)

apiDir = Path(basedir).parent.absolute()
fileDir = os.path.join(apiDir.absolute(),'files')

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'relative/path/to/file/you/want')


@image_bp.route('/api/img/<id>', methods=['GET'])
def get_pelicula(id):
    # return id
    print(os.path.join(fileDir, f'{id}.png'))
    return send_file(os.path.join(fileDir, f'{id}.png'), mimetype='json', as_attachment=False, 
    download_name=None, attachment_filename=None, conditional=True, etag=True, add_etags=None, last_modified=None, max_age=None, cache_timeout=None)
    # return send_from_directory(
    #     fileDir, id, as_attachment=True
    # )


# @image_bp.route('/api/pelicula', methods=['GET'])
# def query_pelicula():
#     pelicula = peliculaService.query_pelicula()
#     output = peliculasSchema.dump(pelicula)
#     return jsonify(output)
