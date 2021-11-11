from ..Model.AsientoModel import AsientoSchema
from ..Model.AsientoModel import AsientoSchema
from flask import Blueprint , Response , jsonify ,current_app as app
from flask.globals import request
from marshmallow import Schema, fields, ValidationError
from ..Logic.emailService import sendmail
from ..Logic import compraService
from ..Logic import ticketService
from http import HTTPStatus
import json


# Blueprint Configuration
compra_bp = Blueprint(
    'compra_bp', __name__
)
compraSchema = AsientoSchema()
comprasSchema = AsientoSchema(many=True)



@compra_bp.route('/api/compra', methods=['POST'])
def compra():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No data provided"}, 400
    # Validate and deserialize input
    try:
        precioIdQuantityList = json_data['precioIdQuantitySelected']
        asientosId = json_data['asientoIdSelected']
        funcionId  = json_data['funcionId']
        email = json_data['email']
        nombre = json_data['nombre']
        cont = 0
        ticketIdList=[]
        for e in precioIdQuantityList:
            for x in range(e['quantity']):
                asientoId = asientosId[cont]
                ticketId = ticketService.create_ticket(asientoId,e['precioId'],email,nombre)
                ticketIdList.append(ticketId)
                cont += 1
        compra = compraService.compra(funcionId,ticketIdList,email,nombre)
        sendmail(compraService.get_compra(compra))
    except ValueError as e :
        print(e)
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
   

    return Response('{"data": "JSON string example"}',headers=dict({
    "HeaderExample": "HeaderContent"
    }),mimetype="application/json")

@compra_bp.route('/api/compra', methods=['GET'])
def compra_get():
    # Validate and deserialize input
    try:
        compra = compraService.get_compra(7)
        sendmail(compra)
    except ValueError as e :
        print(e)
        return Response(mimetype="application/json",status=HTTPStatus.INTERNAL_SERVER_ERROR,response=json.dumps({"message":str(e)}))
   

    return Response('{"data": "JSON string example"}',headers=dict({
    "HeaderExample": "HeaderContent"
    }),mimetype="application/json")