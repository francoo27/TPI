from flask.globals import request
import os
from flask import Blueprint , Response , jsonify ,current_app as app
from flask import send_file,send_from_directory,flash, request, redirect, url_for
from werkzeug.utils import secure_filename
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

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

@image_bp.route('/api/img/<id>', methods=['GET'])
def get_image(id):
    # return id
    print(os.path.join(fileDir, f'{id}'))
    return send_file(os.path.join(fileDir, f'{id}'), mimetype='json', as_attachment=False, 
    download_name=None, attachment_filename=None, conditional=True, etag=True, add_etags=None, last_modified=None, max_age=None, cache_timeout=None)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS   

@image_bp.route('/api/img', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    print(request.headers)
    print(request.files)
    if 'file' not in request.files:
        return {"message": "No data provided"}, 400
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return {"message": "No selected file"}, 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(fileDir, filename))
        return {"message": "Image Uploaded"}, 200