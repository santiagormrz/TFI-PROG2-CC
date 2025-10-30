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
    def establecerNumeroId(self, numId:int):
        self.numId=numId
    def establecerFecha(self, fecha:str):
        self.fecha=fecha
    def establecerClienteId(self, clienteId:int):
        self.clienteId=clienteId
    def establecerVehiculoId(self, vehiculoId:int):
        self.vehiculoId=vehiculoId
    def establecerMonto(self, monto:int):
        self.monto=monto


    #Consultas
    def obtenerNumeroId(self):
        return self.numId
    def obtenerFecha(self):
        return self.fecha
    def obtenerClienteId(self):
        return self.clienteId
    def obtenerVehiculoId(self):
        return self.vehiculoId
    def obtenerMonto(self):
        return self.monto
    def __eq__(self, numId):
        return self.numId==numId.obtenerNumeroId()
    def __str__(self):
        return f'ID: {self.numId} -- Fecha: {self.fecha} -- Cliente ID: {self.clienteId} -- Vehiculo ID: {self.vehiculoId} -- Monto: ${self.monto}'

venta1=Venta(1,'2023-10-01',101,201,15000)
venta2=Venta(2,'10-5-2025',100,256,50000)
print(venta1.__str__())
print(venta1.__eq__(venta2))
