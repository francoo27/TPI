from ..Data import ticketRepository
from ..Model.TicketModel import Ticket

def get_ticket(id):
    return ticketRepository.get_ticket(id)

def create_ticket(idAsiento,idPrecio,email,nombre):
    ticket = Ticket()
    ticket.id_asiento = idAsiento
    ticket.id_precio = idPrecio
    ticket.email = email
    ticket.nombre = nombre
    return ticketRepository.create_ticket(ticket)