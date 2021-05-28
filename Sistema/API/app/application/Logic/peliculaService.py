from ..Data import peliculaRepository
from ..Model.PeliculaModel import Pelicula

def get_pelicula(id):
    return peliculaRepository.get_pelicula(id)

def query_pelicula():
    return peliculaRepository.query_pelicula()

def pelicula_create(pelicula):
    pelicula = Pelicula(nombre = pelicula.nombre)
    peliculaRepository.pelicula_create(pelicula)

def pelicula_update(pelicula):
    peliculaRepository.pelicula_update(pelicula)

def pelicula_delete(id):
    peliculaRepository.pelicula_delete(id)
    