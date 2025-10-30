class Cliente:
    #Constructor 
    def __init__(self, numid:int, nom:str, apell:str, mail:str):
        #Atributos de instancia
        self.numeroid=numid
        self.nombres=nom
        self.apellido=apell
        self.email=mail

    #Comandos
    def establecerNumeroid(self, num:int):
        self.numeroid=num
    def establcerNombres(self, nom:str):
        self.nombres=nom
    def establecerApellido(self, apell:str):
        self.apellido=apell
    def establecerEmail(self, mail:str):
        self.email=mail

    #Consultas
    def obtenerNumeroid(self):
        return self.numeroid
    def obtenerNombres(self):
        return self.nombres
    def obtenerApellido(self):
        return self.apellido
    def obtenerEmail(self):
        return self.email
    def __eq__(self, numId):
        return self.numeroid==numId.obtenerNumeroid()
    def __str__(self):
        return f'ID: {self.numeroid} -- Nombre: {self.nombres} -- Apellido: {self.apellido} -- Email: {self.email}'
    

cliente1=Cliente(1, 'Axel', 'Morales', 'llolo@gmail.com')
cliente2=Cliente(2,'Luis', 'Perez', 'mmmmm@gmail.com')
print(cliente1.__str__())
print(cliente1.__eq__(cliente2))