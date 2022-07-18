class Cliente:
   def __init__(self, nombre, apellido, numero, dni, transacciones = [], direccion = None):
         self.nombre=nombre
         self.apellido=apellido
         self.numero=numero
         self.dni=dni
         self.transacciones = transacciones
         self.__direccion = direccion

   @property
   def direccion(self):
      return self.__direccion

   @direccion.setter
   def direccion(self, direccion):
      self.__direccion = direccion

   def guardarInfo(self):
      objInfo = {
         "nombre": self.nombre,
         "apellido": self.apellido,
         "numero": self.numero,
         "dni": self.dni,
         "direccion": [self.direccion.calle, self.direccion.numero,self.direccion.ciudad,self.direccion.provincia, self.direccion.pais],
         "motivo": ""
      }

   def puede_crear_chequera(self):
      pass

   def puede_crear_tarjeta_credito(self):
      pass

   def puede_comprar_dolar(self):
      pass