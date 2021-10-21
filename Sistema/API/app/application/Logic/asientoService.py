from ..Data import asientoRepository
from ..Model.AsientoModel import Asiento

def query_ocupados_by_funcion(id):
    return asientoRepository.query_ocupados_by_funcion(id)
    