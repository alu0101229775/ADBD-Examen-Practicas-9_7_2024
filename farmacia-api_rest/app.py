###############################################################################
#########         GERARD ANTONY CARAMAZZA VILÁ (45983867J)            #########
#########                 EXAMEN ADBD 09/07/2024                      #########
###############################################################################

# Configuración de la aplicación Flask y definición de las rutas para las operaciones CRUD.

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import models

app = Flask(__name__)
api = Api(app)

class MedicamentoList(Resource):
    def get(self):
        medicamentos = models.get_all_medicamentos()
        return jsonify(medicamentos)

    def post(self):
        medicamento = request.get_json()
        models.create_medicamento(medicamento)
        return {"message": "Medicamento creado"}, 201

class Medicamento(Resource):
    def get(self, codigo_medicamento):
        medicamento = models.get_medicamento(codigo_medicamento)
        if medicamento:
            return jsonify(medicamento)
        return {"message": "Medicamento no encontrado"}, 404

    def put(self, codigo_medicamento):
        medicamento = request.get_json()
        models.update_medicamento(codigo_medicamento, medicamento)
        return {"message": "Medicamento actualizado"}, 200

    def delete(self, codigo_medicamento):
        models.delete_medicamento(codigo_medicamento)
        return {"message": "Medicamento eliminado"}, 200

class LaboratorioList(Resource):
    def get(self):
        laboratorios = models.get_all_laboratorios()
        return jsonify(laboratorios)

    def post(self):
        laboratorio = request.get_json()
        models.create_laboratorio(laboratorio)
        return {"message": "Laboratorio creado"}, 201

class Laboratorio(Resource):
    def get(self, codigo_laboratorio):
        laboratorio = models.get_laboratorio(codigo_laboratorio)
        if laboratorio:
            return jsonify(laboratorio)
        return {"message": "Laboratorio no encontrado"}, 404

    def put(self, codigo_laboratorio):
        laboratorio = request.get_json()
        models.update_laboratorio(codigo_laboratorio, laboratorio)
        return {"message": "Laboratorio actualizado"}, 200

    def delete(self, codigo_laboratorio):
        models.delete_laboratorio(codigo_laboratorio)
        return {"message": "Laboratorio eliminado"}, 200

class FamiliaList(Resource):
    def get(self):
        familias = models.get_all_familias()
        return jsonify(familias)

    def post(self):
        familia = request.get_json()
        models.create_familia(familia)
        return {"message": "Familia creada"}, 201

class Familia(Resource):
    def get(self, codigo_familia):
        familia = models.get_familia(codigo_familia)
        if familia:
            return jsonify(familia)
        return {"message": "Familia no encontrada"}, 404

    def put(self, codigo_familia):
        familia = request.get_json()
        models.update_familia(codigo_familia, familia)
        return {"message": "Familia actualizada"}, 200

    def delete(self, codigo_familia):
        models.delete_familia(codigo_familia)
        return {"message": "Familia eliminada"}, 200

class ClienteList(Resource):
    def get(self):
        clientes = models.get_all_clientes()
        return jsonify(clientes)

    def post(self):
        cliente = request.get_json()
        models.create_cliente(cliente)
        return {"message": "Cliente creado"}, 201

class Cliente(Resource):
    def get(self, codigo_cliente):
        cliente = models.get_cliente(codigo_cliente)
        if cliente:
            return jsonify(cliente)
        return {"message": "Cliente no encontrado"}, 404

    def put(self, codigo_cliente):
        cliente = request.get_json()
        models.update_cliente(codigo_cliente, cliente)
        return {"message": "Cliente actualizado"}, 200

    def delete(self, codigo_cliente):
        models.delete_cliente(codigo_cliente)
        return {"message": "Cliente eliminado"}, 200

class ClienteConCreditoList(Resource):
    def get(self):
        clientes_con_credito = models.get_all_clientes_con_credito()
        return jsonify(clientes_con_credito)

    def post(self):
        cliente_con_credito = request.get_json()
        models.create_cliente_con_credito(cliente_con_credito)
        return {"message": "Cliente con crédito creado"}, 201

class ClienteConCredito(Resource):
    def get(self, codigo_cliente):
        cliente_con_credito = models.get_cliente_con_credito(codigo_cliente)
        if cliente_con_credito:
            return jsonify(cliente_con_credito)
        return {"message": "Cliente con crédito no encontrado"}, 404

    def put(self, codigo_cliente):
        cliente_con_credito = request.get_json()
        models.update_cliente_con_credito(codigo_cliente, cliente_con_credito)
        return {"message": "Cliente con crédito actualizado"}, 200

    def delete(self, codigo_cliente):
        models.delete_cliente_con_credito(codigo_cliente)
        return {"message": "Cliente con crédito eliminado"}, 200

class ClienteSinCreditoList(Resource):
    def get(self):
        clientes_sin_credito = models.get_all_clientes_sin_credito()
        return jsonify(clientes_sin_credito)

    def post(self):
        cliente_sin_credito = request.get_json()
        models.create_cliente_sin_credito(cliente_sin_credito)
        return {"message": "Cliente sin crédito creado"}, 201

class ClienteSinCredito(Resource):
    def get(self, codigo_cliente):
        cliente_sin_credito = models.get_cliente_sin_credito(codigo_cliente)
        if cliente_sin_credito:
            return jsonify(cliente_sin_credito)
        return {"message": "Cliente sin crédito no encontrado"}, 404

    def delete(self, codigo_cliente):
        models.delete_cliente_sin_credito(codigo_cliente)
        return {"message": "Cliente sin crédito eliminado"}, 200

class DatosBancariosList(Resource):
    def get(self):
        datos_bancarios = models.get_all_datos_bancarios()
        return jsonify(datos_bancarios)

    def post(self):
        dato_bancario = request.get_json()
        models.create_datos_bancarios(dato_bancario)
        return {"message": "Dato bancario creado"}, 201

class DatosBancarios(Resource):
    def get(self, codigo_datos_bancarios):
        dato_bancario = models.get_datos_bancarios(codigo_datos_bancarios)
        if dato_bancario:
            return jsonify(dato_bancario)
        return {"message": "Dato bancario no encontrado"}, 404

    def put(self, codigo_datos_bancarios):
        dato_bancario = request.get_json()
        models.update_datos_bancarios(codigo_datos_bancarios, dato_bancario)
        return {"message": "Dato bancario actualizado"}, 200

    def delete(self, codigo_datos_bancarios):
        models.delete_datos_bancarios(codigo_datos_bancarios)
        return {"message": "Dato bancario eliminado"}, 200

class VentaList(Resource):
    def get(self):
        ventas = models.get_all_ventas()
        return jsonify(ventas)

    def post(self):
        venta = request.get_json()
        models.create_venta(venta)
        return {"message": "Venta creada"}, 201

class Venta(Resource):
    def get(self, codigo_venta):
        venta = models.get_venta(codigo_venta)
        if venta:
            return jsonify(venta)
        return {"message": "Venta no encontrada"}, 404

    def put(self, codigo_venta):
        venta = request.get_json()
        models.update_venta(codigo_venta, venta)
        return {"message": "Venta actualizada"}, 200

    def delete(self, codigo_venta):
        models.delete_venta(codigo_venta)
        return {"message": "Venta eliminada"}, 200

class PagoList(Resource):
    def get(self):
        pagos = models.get_all_pagos()
        return jsonify(pagos)

    def post(self):
        pago = request.get_json()
        models.create_pago(pago)
        return {"message": "Pago creado"}, 201

class Pago(Resource):
    def get(self, codigo_pago):
        pago = models.get_pago(codigo_pago)
        if pago:
            return jsonify(pago)
        return {"message": "Pago no encontrado"}, 404

    def put(self, codigo_pago):
        pago = request.get_json()
        models.update_pago(codigo_pago, pago)
        return {"message": "Pago actualizado"}, 200

    def delete(self, codigo_pago):
        models.delete_pago(codigo_pago)
        return {"message": "Pago eliminado"}, 200

api.add_resource(MedicamentoList, '/medicamentos')
api.add_resource(Medicamento, '/medicamentos/<int:codigo_medicamento>')
api.add_resource(LaboratorioList, '/laboratorios')
api.add_resource(Laboratorio, '/laboratorios/<int:codigo_laboratorio>')
api.add_resource(FamiliaList, '/familias')
api.add_resource(Familia, '/familias/<int:codigo_familia>')
api.add_resource(ClienteList, '/clientes')
api.add_resource(Cliente, '/clientes/<int:codigo_cliente>')
api.add_resource(ClienteConCreditoList, '/clientes_con_credito')
api.add_resource(ClienteConCredito, '/clientes_con_credito/<int:codigo_cliente>')
api.add_resource(ClienteSinCreditoList, '/clientes_sin_credito')
api.add_resource(ClienteSinCredito, '/clientes_sin_credito/<int:codigo_cliente>')
api.add_resource(DatosBancariosList, '/datos_bancarios')
api.add_resource(DatosBancarios, '/datos_bancarios/<int:codigo_datos_bancarios>')
api.add_resource(VentaList, '/ventas')
api.add_resource(Venta, '/ventas/<int:codigo_venta>')
api.add_resource(PagoList, '/pagos')
api.add_resource(Pago, '/pagos/<int:codigo_pago>')

if __name__ == '__main__':
    app.run(debug=True)
