from ..Data import clasificacionRepository
from ..Model.ClasificacionModel import Clasificacion

def get_clasificacion(id):
    return clasificacionRepository.get_clasificacion(id)

def query_clasificacion():
    return clasificacionRepository.query_clasificacion()
    