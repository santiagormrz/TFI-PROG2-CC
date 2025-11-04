#EJERCICIO 2

class Cliente:
    #Constructor 
    def __init__(self, numero_id:int, nombres:str, apellidos:str, email:str):
        #Atributos de instancia privados
        self.__numero_id = numero_id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__email = email

    #Comandos
    def establecer_numero_id(self, numero_id:int):
        self.__numero_id = numero_id
    def establecer_nombres(self, nombres:str):
        self.__nombres = nombres
    def establecer_apellidos(self, apellidos:str):
        self.__apellidos = apellidos
    def establecer_email(self, email:str):
        self.__email = email

    #Consultas
    def obtener_numero_id(self):
        return self.__numero_id
    def obtener_nombres(self):
        return self.__nombres
    def obtener_apellidos(self):
        return self.__apellidos
    def obtener_email(self):
        return self.__email
    
    def __eq__(self, otro_cliente):
        return self.__numero_id == otro_cliente.obtener_numero_id()
    
    def __str__(self):
        return f'ID: {self.__numero_id} -- Nombre: {self.__nombres} -- Apellido: {self.__apellidos} -- Email: {self.__email}'