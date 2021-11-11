from http import HTTPStatus
import json
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from flask import abort
from ..Logic import authorizationService
from ..Data import authorizationRepository
from ..Model.UsuarioModel import Usuario , UsuarioSchema
from marshmallow import Schema, fields, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from jwt import encode, decode
import datetime

# Blueprint Configuration
authorization_bp = Blueprint(
    'authorization_bp', __name__
)

usuarioSchema = UsuarioSchema()
@authorization_bp.route('/api/authorization/register', methods=['GET', 'POST'])
def signup_user():  
    data = request.get_json()  

    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    nuevo_usuario = Usuario(public_id=str(uuid.uuid4()), nombre=data['nombre'], password=hashed_password, admin=False,gerente=False)
    authorizationService.register(nuevo_usuario) 
    return jsonify({'message': 'registered successfully'})

@authorization_bp.route('/api/authorization/login', methods=['POST'])  
def login_user():
    data = request.get_json()  
    print(data) 
    if  not data['email'] or not data['password']:
        return {'WWW.Authentication': 'Basic realm: "login required"'} , 401

    token = authorizationRepository.login(data['email'],data['password'])
    print(token)
    if token is None:
        return Response(mimetype="application/json",status=HTTPStatus.ACCEPTED,response=json.dumps({"token":""}))
    return Response(mimetype="application/json",status=HTTPStatus.ACCEPTED,response=json.dumps({"token":token}))

@authorization_bp.route('/api/authorization/logout', methods=['POST'])  
def logout_user():
    data = request.get_json()
    print(data) 
    if  not data['token']:
        return {'WWW.Authentication': 'Basic realm: "login required"'} , 401

    # authorizationRepository.logout(data['token'])

    return Response(mimetype="application/json",status=HTTPStatus.ACCEPTED)

@authorization_bp.route('/api/authorization/<token>', methods=['GET'])  
def auth_user(token):
    print(token) 
    if  not token or token == "" or token == "null":
        return {'WWW.Authentication': 'Basic realm: "login required"'} , 401

    if authorizationRepository.auth(token) is False:
        abort(401)  

    return Response(mimetype="application/json",status=HTTPStatus.ACCEPTED)