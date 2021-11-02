from ..Data import generoRepository
from ..Logic import peliculaService
from ..Model.GeneroModel import Genero

def get_genero(id):
    return generoRepository.get_genero(id)

def query_genero():
    return generoRepository.query_genero()

def genero_create(genero):
    return generoRepository.genero_create(genero)

def genero_update(genero):
    return generoRepository.genero_update(genero)

def genero_delete(generoId):
    print(peliculaService.any_pelicula_has_genero(generoId))
    if peliculaService.any_pelicula_has_genero(generoId):
        raise ValueError('No es posible eliminar un Genero vinculada a una pelicula')
    else:
        generoRepository.genero_delete(generoId)

    