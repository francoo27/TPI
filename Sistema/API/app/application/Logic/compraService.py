from ..Data import compraRepository
from ..Logic import ticketService
from ..Model.PrecioModel import Precio


def compra(email,funcionId,ticketsIdList):
    tickets = []
    for t in ticketsIdList:
        tickets.append(ticketService.get_ticket(t))
    compraRepository.compra(email,funcionId,tickets)
    