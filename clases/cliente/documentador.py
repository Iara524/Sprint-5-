import webbrowser

#En el reporte se debe incluir el nombre de cliente, número, DNI, dirección y para cada transacción la fecha , el tipo de operación, el estado, el monto y razón por la cual se rechazó (vacío en caso de ser aceptada).
class Documentador:
    
    def crear_html(nombre,apellido,numero,dni,direccion,fecha,tipo,estado,monto,razon):

        f = open('reporte.html','w')

        mensaje = """<html>
        <head>
        </head>
        <body><p>"""+str(nombre)+" "+str(apellido)+" "+str(numero)+" "+str(dni)+"</br>"+str(direccion)+"</br>"+str(fecha)+" "+str(tipo)+" "+str(estado)+" "+str(monto)+" "+str(razon)+"""</p>
        </body></html>"""

        f.write(mensaje)
        f.close()

        webbrowser.open_new_tab('reporte.html')
