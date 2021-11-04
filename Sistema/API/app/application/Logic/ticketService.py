from ..Data import ticketRepository
from ..Model.TicketModel import Ticket

def get_ticket(id):
    return ticketRepository.get_ticket(id)

def create_ticket(idAsiento,idPrecio):
    ticket = Ticket()
    ticket.id_asiento = idAsiento
    ticket.id_precio = idPrecio
    return ticketRepository.create_ticket(ticket)