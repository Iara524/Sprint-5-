from .cliente import Cliente

class ClienteGold(Cliente):
    def __init__(self, nombre,apellido,numero,dni) -> None:
        super().__init__(nombre,apellido,numero,dni)
        self.tajeta_debito = 1
        self.caja_ahorro = "dolares"
        self.descubierto_corriente = 10000
        self.cuenta_corriente = True
        self.max_cajero = 20000
        self.min_corriente = -10000
        self.caja_dolares = True
        self.tajeta_credito = 1
        self.alta_chequera = 1
        self.comsion_transf = 0.05
        self.max_transferencia = 500000

    def puede_crear_chequera(self):
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ALTA_CHEQUERA":
                transaccion["totalChequerasActualmente"] += 1
                if self.max_chequera >= transaccion["totalChequerasActualmente"]:
                    print("Puede tener chequera")
                else:
                    print("No puede crear cherquera")

    def puede_crear_tarjeta_credito(self):
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ALTA_TARJETA_CREDITO":
                transaccion["totalTarjetasDeCreditoActualmente"] += 1
                if self.tajeta_credito >= transaccion["totalTarjetasDeCreditoActualmente"]:
                    return True

    def saldo_maximo(self):
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                if (transaccion["cupoDiarioRestante"] - transaccion["monto"]) >= self.min_corriente:
                    print("Tenes cash")
                else:
                    print("No se puede realizar la transacción")
