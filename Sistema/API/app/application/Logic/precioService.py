from ..Data import precioRepository
from ..Model.PrecioModel import Precio


def query_precio():
    return precioRepository.query_precio()

def get_precio(id):
    return precioRepository.get_precio(id)
    