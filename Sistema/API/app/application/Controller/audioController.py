from http import HTTPStatus
import json
from ..Model.AudioModel import AudioSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import audioService
from marshmallow import Schema, fields, ValidationError
from ..Shared import db


# Blueprint Configuration
audio_bp = Blueprint(
    'audio_bp', __name__
)
audioSchema = AudioSchema()
audiosSchema = AudioSchema(many=True)


@audio_bp.route('/api/audio/<id>', methods=['GET'])
def get_audio(id):
    audio =  audioService.get_audio(id)
    output = audioSchema.dump(audio)
    return jsonify(output)


@audio_bp.route('/api/audio', methods=['GET'])
def query_audio():
    audio = audioService.query_audio()
    output = audiosSchema.dump(audio)
    return jsonify(output)


@audio_bp.route('/api/audio', methods=['POST'])
def audio_create():
    if request.data:
        json_data = request.get_json()
    else:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        data = audioSchema.load(json_data)
    except Exception as e :
        print(e)
        return {e: "Error"}, 422
    try:
        audioService.audio_create(data)
    except ValueError as e :
        return {e: "Error"}, 400
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@audio_bp.route('/api/audio/<id>', methods=['PUT'])
def audio_update(id):
    json_data = request.get_json()
    print(json_data)
    if not json_data:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        # WORKAROUND https://www.gitmemory.com/issue/marshmallow-code/flask-marshmallow/44/508944019
        data = audioSchema.load(json_data,session=db.session)
    except Exception as e :
        return {"message": "Error"}, 422
    audioService.audio_update(data)
    return Response(headers=dict({
  "HeaderExample": "HeaderContent"
}),mimetype="application/json")


@audio_bp.route('/api/audio/<id>', methods=['DELETE'])
def audio_delete(id):
    try:
        audioService.audio_delete(id)
    except ValueError as e :
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
    return Response(headers=dict({
    "HeaderExample": "HeaderContent"
    }),mimetype="application/json")