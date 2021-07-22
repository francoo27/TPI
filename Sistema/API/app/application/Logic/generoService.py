from ..Data import generoRepository
from ..Model.GeneroModel import Genero

def get_genero(id):
    return generoRepository.get_genero(id)

def query_genero():
    return generoRepository.query_genero()
    