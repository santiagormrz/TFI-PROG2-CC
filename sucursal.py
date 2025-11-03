# EJERCICIO 1

from venta import Venta

class Sucursal:
    def __init__(self, numero_id, nombre, ventas):
        # atributos privados
        self.__numero_id = numero_id
        self.__nombre = nombre
        self.__ventas = ventas

    # métodos de acceso
    def obtener_numero_id(self):
        return self.__numero_id

    def obtener_nombre(self):
        return self.__nombre

    def obtener_ventas(self):
        return self.__ventas

    # métodos de comando 
    def agregar_venta(self, venta):
        # agrega una venta a la lista de ventas
        self.__ventas.append(venta)

    # métodos especiales
    def __eq__(self, otra_sucursal):
        # Compara dos sucursales por numero_id
        return self.__numero_id == otra_sucursal.obtener_numero_id()

    def __str__(self):
        # muestra todos los datos de la sucursal
        texto_ventas = ""
        if len(self.__ventas) == 0:
            texto_ventas = "Sin ventas registradas"
        else:
            for v in self.__ventas:
                texto_ventas += str(v) + "\n"
        return "Sucursal ID: " + str(self.__numero_id) + "\nNombre: " + self.__nombre + "\nVentas:\n" + texto_ventas

