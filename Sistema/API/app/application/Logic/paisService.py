
from ..Data import paisRepository
def create_pais(nombre):
    print('pais logic layer accesed')
    paisRepository.create_pais(nombre)