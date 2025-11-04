# EJERCICIO 1

from venta import Venta

class Sucursal:
    def __init__(self, numero_id, direccion):
        
        self.__numero_id = numero_id
        self.__direccion = direccion
        self.__ventas = []

    
    def obtener_numero_id(self):
        return self.__numero_id

    def obtener_direccion(self):
        return self.__direccion

    def obtener_ventas(self):
        return self.__ventas

    
    def agregar_venta(self, venta):
        
        self.__ventas.append(venta)

    
    def __eq__(self, otra_sucursal):
        
        return self.__numero_id == otra_sucursal.obtener_numero_id()

    def __str__(self):
        
        texto_ventas = ""
        if len(self.__ventas) == 0:
            texto_ventas = "Sin ventas registradas"
        else:
            for v in self.__ventas:
                texto_ventas += str(v) + "\n"
        return "Sucursal ID: " + str(self.__numero_id) + "\nDirección: " + self.__direccion + "\nVentas:\n" + texto_ventas

