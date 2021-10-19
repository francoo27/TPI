from ..Data import precioRepository
from ..Model.PrecioModel import Precio


def query_precio():
    return precioRepository.query_precio()
    