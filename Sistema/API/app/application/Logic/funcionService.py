from ..Data import funcionRepository
from ..Model.FuncionModel import Funcion

def get_funcion(id):
    return funcionRepository.get_funcion(id)

def query_funcion():
    return funcionRepository.query_funcion()

def query_ByPeliculaAndFormato(peliculaId,fomatoId):
    return funcionRepository.query_ByPeliculaAndFormato(peliculaId,fomatoId)

def funcion_create(funcion):
    # funcion = Funcion(nombre = funcion.nombre)
    funcionRepository.funcion_create(funcion)

def funcion_update(funcion):
    funcionRepository.funcion_update(funcion)

def funcion_delete(id):
    funcionRepository.funcion_delete(id)

def funcion_cancel(id):
    funcionRepository.funcion_cancel(id)
    