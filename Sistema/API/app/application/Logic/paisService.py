from ..Data import paisRepository
from ..Model.PaisModel import Pais

def get_pais(id):
    return paisRepository.get_pais(id)

def query_pais():
    return paisRepository.query_pais()

def pais_create(nombre):
    pais = Pais(nombre)
    pais.nombre = nombre
    paisRepository.pais_create(pais)

def pais_update(id, nombre):
    paisRepository.pais_update(id, nombre)

def pais_delete(id):
    paisRepository.pais_delete(id)
    