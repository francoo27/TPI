from functools import wraps
from flask import abort
import jwt
from flask import request
from ...Data import authorizationRepository

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
            # print(request.headers['Authorization'])
            # # print(authorizationRepository.login("a@a.com","a"))
            if not 'Authorization' in request.headers:
                abort(401)
            if authorizationRepository.auth(request.headers['Authorization']) is None:
                abort(401)

            return f(*args, **kws)            
    return decorated_function