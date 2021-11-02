from ..Data import clasificacionRepository
from ..Logic import peliculaService

def get_clasificacion(id):
    return clasificacionRepository.get_clasificacion(id)

def query_clasificacion():
    return clasificacionRepository.query_clasificacion()

def clasificacion_create(clasificacion):
    return clasificacionRepository.clasificacion_create(clasificacion)

def clasificacion_update(clasificacion):
    return clasificacionRepository.clasificacion_update(clasificacion)

def clasificacion_delete(clasificacionId):
    if peliculaService.any_pelicula_has_clasificacion(clasificacionId):
        raise ValueError('No es posible eliminar un Clasificacion vinculada a una pelicula')
    else:
        clasificacionRepository.clasificacion_delete(clasificacionId)
