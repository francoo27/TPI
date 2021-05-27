from ..Data import paisRepository
from ..Model.PaisModel import Pais

def get_pais(id):
    return paisRepository.get_pais(id)

def query_pais():
    return paisRepository.query_pais()

def pais_create(pais):
    pais = Pais(nombre = pais.nombre)
    paisRepository.pais_create(pais)

def pais_update(pais):
    paisRepository.pais_update(pais)

def pais_delete(id):
    paisRepository.pais_delete(id)
    