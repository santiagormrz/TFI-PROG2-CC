#EJERCICIO 4

class Venta:
    #Constructor 
    def __init__(self, numero_id:int, fecha:str, cliente_id:int, vehiculo_id:int, monto:int):
        #Atributos de instancia privados
        self.__numero_id = numero_id
        self.__fecha = fecha
        self.__cliente_id = cliente_id
        self.__vehiculo_id = vehiculo_id
        self.__monto = monto

    #Comandos
    def establecer_numero_id(self, numero_id:int):
        self.__numero_id = numero_id
    def establecer_fecha(self, fecha:str):
        self.__fecha = fecha
    def establecer_cliente_id(self, cliente_id:int):
        self.__cliente_id = cliente_id
    def establecer_vehiculo_id(self, vehiculo_id:int):
        self.__vehiculo_id = vehiculo_id
    def establecer_monto(self, monto:int):
        self.__monto = monto

    #Consultas
    def obtener_numero_id(self):
        return self.__numero_id
    def obtener_fecha(self):
        return self.__fecha
    def obtener_cliente_id(self):
        return self.__cliente_id
    def obtener_vehiculo_id(self):
        return self.__vehiculo_id
    def obtener_monto(self):
        return self.__monto
    
    def __eq__(self, otra_venta):
        return self.__numero_id == otra_venta.obtener_numero_id()
    
    def __str__(self):
        return f'ID: {self.__numero_id} -- Fecha: {self.__fecha} -- Cliente ID: {self.__cliente_id} -- Vehiculo ID: {self.__vehiculo_id} -- Monto: ${self.__monto}'