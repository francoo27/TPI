from ..Model.AsientoModel import AsientoSchema
from ..Model.AsientoModel import AsientoSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from marshmallow import Schema, fields, ValidationError
from ..Logic.emailService import sendmail
from ..Logic import compraService
from ..Logic import ticketService


# Blueprint Configuration
compra_bp = Blueprint(
    'compra_bp', __name__
)
compraSchema = AsientoSchema()
comprasSchema = AsientoSchema(many=True)



@compra_bp.route('/api/compra', methods=['POST'])
def compra():
    data = request.get_json()
    precioIdQuantityList = data['precioIdQuantitySelected']
    asientosId = data['asientoIdSelected']
    cont = 0
    ticketIdList=[]
    for e in precioIdQuantityList:
        for x in range(e['quantity']):
            asientoId = asientosId[cont]
            ticketId = ticketService.create_ticket(asientoId,e['precioId'])
            ticketIdList.append(ticketId)
            cont += 1
    compraService.compra("a@a.com",5,ticketIdList)
    # print(compra)
    # comprasSchema.dump_only
    # ticket = ticketService.create_ticket(1,1)
    # print(ticket)
    return Response('{"data": "JSON string example"}',headers=dict({
    "HeaderExample": "HeaderContent"
    }),mimetype="application/json")
