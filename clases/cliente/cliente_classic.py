from .cliente import Cliente

class ClienteClassic(Cliente):
    def __init__(self, nombre,apellido,numero,dni) -> None:
        super().__init__(nombre,apellido,numero,dni)
        self.tajeta_debito = 1
        self.caja_ahorro = "pesos"
        self.cuenta_corriente = False
        self.max_cajero = 10000
        self.tajeta_credito = 0
        self.caja_dolares = False
        self.alta_chequera = 0
        self.comsion_transf = 0.1
        self.max_transferencia = 150000

    def puede_crear_chequera(self):
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ALTA_CHEQUERA":
                transaccion["totalChequerasActualmente"] += 1
                if self.max_chequera >= transaccion["totalChequerasActualmente"]:
                    return True
                else:
                    motivo1 = "No puede tener más chequeras"
                    return motivo1

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
