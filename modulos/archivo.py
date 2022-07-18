import json
from clases import ClienteClassic, ClienteBlack, ClienteGold
from clases.direccion.direccion import Direccion


class Archivo:

    def abrir_archivo(self, archivo):
        self.archivo = archivo
        file = open(self.archivo, encoding='utf-8')
        data = json.load(file)

        if(data['tipo']=="BLACK"):
            data_info = ClienteBlack(data['nombre'], data['apellido'], data['numero'], data['DNI'], data["transacciones"])
            data_info.direccion = Direccion("Libertador", "7900", "Capital Federal", "Buenos Aires", "Argentina")
            data_info.puede_crear_chequera()
            data_info.saldo_maximo()


        if(data['tipo']=="CLASSIC"):
            cliente_classic = ClienteClassic(data['nombre'], data['apellido'], data['numero'], data['DNI'])
            return cliente_classic
        if(data['tipo']=="GOLD"):
            cliente_gold = ClienteGold(data['nombre'], data['apellido'], data['numero'], data['DNI'])
            return cliente_gold

        file.close()