import servicio_concesionarias

class ServicioVehiculos:

    def obtener_vehiculos_por_sucursal_y_estado(self, concesionaria_id, sucursal_id, estado_id):
        
        servicio_conc = servicio_concesionarias.ServicioConcesionarias()
        concesionaria = servicio_conc.obtener_por_id(concesionaria_id)

        if concesionaria is None:
            return []
        
        sucursal_existe = False
        
        for sucursal in concesionaria.obtener_sucursales():
            if sucursal.obtener_numero_id() == int(sucursal_id):
                sucursal_existe = True
                break

        if not sucursal_existe:
            return []
        
        vehiculos_encontrados = []

        for vehiculo in concesionaria.obtener_vehiculos():
            if vehiculo.obtener_sucursal_id() == int(sucursal_id) and vehiculo.obtener_estado_id() == int(estado_id):
                vehiculos_encontrados.append(vehiculo)

        return vehiculos_encontrados