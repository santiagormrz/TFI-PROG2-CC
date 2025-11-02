import vehiculo


class Moto(vehiculo.Vehiculo):

    def __init__(
        self, numero_id, marca, modelo, anio, sucursal_id, estado_id, cilindrada
    ):
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
        self.__cilindrada = cilindrada

    def establecer_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def obtener_cilindrada(self):
        return self.__cilindrada
        
    def __str__(self):
        return (
            "Moto ID: "
            + str(self.obtener_numero_id())
            + " - "
            + self.obtener_marca()
            + " "
            + self.obtener_modelo()
            + " ("
            + str(self.obtener_anio())
            + ") "
            + "\nSucursal ID: "
            + str(self.obtener_sucursal_id())
            + " - Estado ID: "
            + str(self.obtener_estado_id())
            + " - Cilindrada: "
            + str(self.__cilindrada)
            + "cc"
        )