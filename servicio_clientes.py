#EJERCICIO 6

import servicio_concesionarias

class ServicioClientes:

    def obtener_total_ventas_por_cliente(self, concesionaria_id, cliente_id):
        
        servicio_conc = servicio_concesionarias.ServicioConcesionarias()
        concesionaria = servicio_conc.obtener_por_id(concesionaria_id)

        if concesionaria is None:
            return 0
        
        cliente_existe = False

        for cliente in concesionaria.obtener_clientes():
            if cliente.obtener_numero_id() == int(cliente_id):
                cliente_existe = True
                break

        if not cliente_existe:
            return 0
        
        total_ventas = 0

        for sucursal in concesionaria.obtener_sucursales():
            for venta in sucursal.obtener_ventas():
                if venta.obtener_cliente_id() == int(cliente_id):
                    total_ventas += venta.obtener_monto()

        return total_ventas


