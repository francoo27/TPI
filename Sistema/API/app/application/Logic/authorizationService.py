from ..Data import authorizationRepository

def register(usuario):
    authorizationRepository.register(usuario)

def get_usuario(id):
    return authorizationRepository.get_usuario(id)

def get_usuario_byName(nombre):
    return authorizationRepository.get_usuario_byName(nombre)
    