from ..Data import compraRepository
from ..Logic import ticketService
from ..Model.PrecioModel import Precio


def compra(funcionId,ticketIdList,email,nombre):
    tickets = []
    for t in ticketIdList:
        tickets.append(ticketService.get_ticket(t))
    return compraRepository.compra(funcionId,tickets,email,nombre)

    