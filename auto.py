#EJERCICIO 3

import vehiculo

class Auto(vehiculo.Vehiculo):

    def __init__(self, numero_id, marca, modelo, anio, sucursal_id, estado_id, airbags, frenos_abs, caballos_fuerza):
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
        self.__airbags = airbags
        self.__frenos_abs = frenos_abs
        self.__caballos_fuerza = caballos_fuerza

    def establecer_airbags(self, airbags):
        self.__airbags = airbags

    def establecer_frenos_abs(self, frenos_abs):
        self.__frenos_abs = frenos_abs

    def establecer_caballos_fuerza(self, caballos_fuerza):
        self.__caballos_fuerza = caballos_fuerza

    def obtener_airbags(self):
        return self.__airbags

    def obtener_frenos_abs(self):
        return self.__frenos_abs

    def obtener_caballos_fuerza(self):
        return self.__caballos_fuerza

    def __str__(self):
        return (
            "Auto ID: "
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
            + " - Airbags: "
            + str(self.__airbags)
            + " - Frenos ABS: "
            + str(self.__frenos_abs)
            + " - Caballos de fuerza: "
            + str(self.__caballos_fuerza)
        )