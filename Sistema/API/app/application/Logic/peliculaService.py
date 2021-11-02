from pickle import TRUE
from ..Data import peliculaRepository
from ..Model.PeliculaModel import Pelicula,PeliculaSchema

peliculaSchema = PeliculaSchema()

def get_pelicula(id):
    return peliculaRepository.get_pelicula(id)

def query_pelicula():
    return peliculaRepository.query_pelicula()

def pelicula_create(pelicula):
    peliculaRepository.pelicula_create(pelicula)

def pelicula_update(pelicula):
    peliculaRepository.pelicula_update(pelicula)

def pelicula_delete(id):
    peliculaRepository.pelicula_delete(id)

def any_pelicula_has_genero(generoId):
    return peliculaRepository.any_pelicula_has_genero(generoId)
    