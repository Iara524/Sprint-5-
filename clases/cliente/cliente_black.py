from pickle import FALSE
from .cliente import Cliente
from .documentador import Documentador
import webbrowser

class ClienteBlack(Cliente):
    def __init__(self, nombre, apellido, numero, dni, transacciones = [], direccion = None):
        super().__init__(nombre,apellido,numero,dni, transacciones, direccion)
        self.tajeta_debito = 1
        self.caja_ahorro = "dolares"
        self.cuenta_corriente = True
        self.descubierto_corriente = 10000
        self.max_cajero = 100000
        self.min_corriente = -10000
        self.caja_dolares = True
        self.tajeta_credito = 5
        self.max_chequera = 2
        self.comsion_transf = 0
        self.max_transferencia = 0
        self.motivo = FALSE
        self.razon = ""

    def puede_crear_chequera(self):
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ALTA_CHEQUERA":
                transaccion["totalChequerasActualmente"] += 1
                if self.max_chequera >= transaccion["totalChequerasActualmente"]:
                    self.razon = " "
                    Documentador.crear_html(self.nombre,self.apellido,self.numero,self.dni,self.direccion,transaccion["fecha"],transaccion["tipo"],transaccion["estado"],transaccion["monto"],self.razon)
                else:
                    self.razon = "YA SE TIENE EL CUPO DE CHEQUERAS DISPONIBLES"
                    Documentador.crear_html(self.nombre,self.apellido,self.numero,self.dni,self.direccion,transaccion["fecha"],transaccion["tipo"],transaccion["estado"],transaccion["monto"],self.razon)


    def puede_crear_tarjeta_credito(self):
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ALTA_TARJETA_CREDITO":
                transaccion["totalTarjetasDeCreditoActualmente"] += 1
                if self.tajeta_credito >= transaccion["totalTarjetasDeCreditoActualmente"]:
                     self.razon = " "
                     Documentador.crear_html(self.nombre,self.apellido,self.numero,self.dni,self.direccion,transaccion["fecha"],transaccion["tipo"],transaccion["estado"],transaccion["monto"],self.razon)
                else:
                    self.razon = "YA SE TIENE EL CUPO DE TARJETAS DE CRÉDITO DISPONIBLES"
                    Documentador.crear_html(self.nombre,self.apellido,self.numero,self.dni,self.direccion,transaccion["fecha"],transaccion["tipo"],transaccion["estado"],transaccion["monto"],self.razon)

    def saldo_maximo(self):
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                if (transaccion["cupoDiarioRestante"] - transaccion["monto"]) >= self.min_corriente:
                    self.razon = " "
                    Documentador.crear_html(self.nombre,self.apellido,self.numero,self.dni,self.direccion,transaccion["fecha"],transaccion["tipo"],transaccion["estado"],transaccion["monto"],self.razon)
                else:
                    self.razon = "SUPERÓ EL LÍMITE DE EXTRACCIÓN"
                    Documentador.crear_html(self.nombre,self.apellido,self.numero,self.dni,self.direccion,transaccion["fecha"],transaccion["tipo"],transaccion["estado"],transaccion["monto"],self.razon)
                
    def puede_comprar_dolar(self):
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "COMPRAR_DOLAR":
                if (transaccion["cupoDiarioRestante"] - transaccion["monto"]) >= self.min_corriente:
                    self.razon = " "
                    Documentador.crear_html(self.nombre,self.apellido,self.numero,self.dni,self.direccion,transaccion["fecha"],transaccion["tipo"],transaccion["estado"],transaccion["monto"],self.razon)

    def transferencia_enviada(self):
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "TRANSFERENCIA_ENVIADA":
                if (  transaccion["monto"] <= transaccion["saldoEnCuenta"]):
                    self.razon = " "
                    Documentador.crear_html(self.nombre,self.apellido,self.numero,self.dni,self.direccion,transaccion["fecha"],transaccion["tipo"],transaccion["estado"],transaccion["monto"],self.razon)
                else:
                    self.razon = "FONDOS INSUFICIENTES"
                    Documentador.crear_html(self.nombre,self.apellido,self.numero,self.dni,self.direccion,transaccion["fecha"],transaccion["tipo"],transaccion["estado"],transaccion["monto"],self.razon)

