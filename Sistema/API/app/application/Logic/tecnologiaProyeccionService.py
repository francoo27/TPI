from ..Data import tecnologiaProyeccionRepository

def tecnologia_proyeccion_create(tecnologiaproyeccion):
    tecnologiaProyeccionRepository.tecnologia_proyeccion_create(tecnologiaproyeccion)

def tecnologia_proyeccion_update(tecnologiaproyeccion):
    tecnologiaProyeccionRepository.tecnologia_proyeccion_update(tecnologiaproyeccion)

def query_tecnologia_proyeccion():
    return tecnologiaProyeccionRepository.query_tecnologia_proyeccion()

def tecnologia_proyeccion_delete(id):
    tecnologiaProyeccionRepository.tecnologia_proyeccion_delete(id)

def get_tecnologia_proyeccion(id):    
    return tecnologiaProyeccionRepository.get_tecnologia_proyeccion(id)

