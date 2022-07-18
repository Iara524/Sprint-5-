class Cliente:
    def __init__(self, nombre, apellido, numero, dni):
        self.nombre=nombre
        self.apellido=apellido
        self.numero=numero
        self.dni=dni
    

    def nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def apellido(self):
        return self.apellido
    
    def set_apellido(self, apellido):
        self.apellido = apellido
    
    def numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero = numero

    def dni(self):
        return self.dni
    
    def set_dni(self, dni):
        self.dni = dni

    def puede_crear_chequera(self):
       return False

    def puede_crear_tarjeta_credito(self):
       return False
    
    def puede_comprar_dolar(self):
       return False


