#EJERCICIO 4
class Venta:
    #Contructor 
    def __init__(self, numId:int, fecha:str, clienteId:int, vehiculoId:int, monto:int):
        #Atributos de instancia
        self.numId=numId
        self.fecha=fecha
        self.clienteId=clienteId
        self.vehiculoId=vehiculoId
        self.monto=monto

    #Comandos
    def establecer_numeroId(self, numId:int):
        self.numId=numId
    def establecer_fecha(self, fecha:str):
        self.fecha=fecha
    def establecer_clienteId(self, clienteId:int):
        self.clienteId=clienteId
    def establecer_vehiculoId(self, vehiculoId:int):
        self.vehiculoId=vehiculoId
    def establecer_monto(self, monto:int):
        self.monto=monto


    #Consultas
    def obtener_numeroId(self):
        return self.numId
    def obtener_fecha(self):
        return self.fecha
    def obtener_clienteId(self):
        return self.clienteId
    def obtener_vehiculoId(self):
        return self.vehiculoId
    def obtener_monto(self):
        return self.monto
    def __eq__(self, numId):
        return self.numId==numId.obtener_numeroId()
    def __str__(self):
        return f'ID: {self.numId} -- Fecha: {self.fecha} -- Cliente ID: {self.clienteId} -- Vehiculo ID: {self.vehiculoId} -- Monto: ${self.monto}'