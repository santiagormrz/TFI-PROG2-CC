#EJERCICIO 2
class Cliente:
    #Constructor 
    def __init__(self, numid:int, nom:str, apell:str, mail:str):
        #Atributos de instancia
        self.numeroid=numid
        self.nombres=nom
        self.apellido=apell
        self.email=mail

    #Comandos
    def establecer_numeroid(self, num:int):
        self.numeroid=num
    def establcer_nombres(self, nom:str):
        self.nombres=nom
    def establecer_apellido(self, apell:str):
        self.apellido=apell
    def establecer_email(self, mail:str):
        self.email=mail

    #Consultas
    def obtener_numeroid(self):
        return self.numeroid
    def obtener_nombres(self):
        return self.nombres
    def obtener_apellido(self):
        return self.apellido
    def obtener_email(self):
        return self.email
    def __eq__(self, numId):
        return self.numeroid==numId.obtener_numeroid()
    def __str__(self):
        return f'ID: {self.numeroid} -- Nombre: {self.nombres} -- Apellido: {self.apellido} -- Email: {self.email}'