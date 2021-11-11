from ..Data import formatoRepository
from ..Model.FormatoModel import Formato

def get_formato(id):
    return formatoRepository.get_formato(id)

def query_formato():
    return formatoRepository.query_formato()

def formato_create(formato):
    print(formato.nombre)
    a = formatoRepository.get_formato_by_name(formato.nombre)
    print(a)
    if a is not None:
        raise ValueError('Ya existe un formato con ese nombre')
    formatoRepository.formato_create(formato)
    

def formato_update(formato):
    currentFormato = formatoRepository.get_formato_by_name(formato.nombre)
    if (currentFormato is not None and formato.id != currentFormato.id):
        raise ValueError('Ya existe un formato con ese nombre')
    formatoRepository.formato_update(formato)

def formato_delete(id):
    formatoRepository.formato_delete(id)
    