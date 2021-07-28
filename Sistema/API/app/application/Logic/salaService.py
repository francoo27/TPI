from ..Data import salaRepository
from ..Model.SalaModel import Sala


def query_sala():
    return salaRepository.query_sala()
    
def query_sala_byComplejo(complejoId):
    return salaRepository.query_sala_byComplejo(complejoId)