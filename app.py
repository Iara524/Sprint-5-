from modulos.archivo import Archivo

archivo_json = input("Ingrese el nombre del archivo JSON: ")

archivo = Archivo()
archivo.abrir_archivo(archivo_json)