from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from ..Logic import authorizationService
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

@authorization_bp.route('/api/authorization/login', methods=['GET', 'POST'])  
def login_user(): 
    auth = request.authorization   

    if not auth or not auth.username or not auth.password:  
        return {'WWW.Authentication': 'Basic realm: "login required"'} , 401

    usuario = authorizationService.get_usuario_byName(auth.username)
        
    if check_password_hash(usuario.password, auth.password):  
        token = encode({'public_id': usuario.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])  
        return jsonify({'token' : token}) 

    return {'WWW.Authentication': 'Basic realm: "login required"'} , 401