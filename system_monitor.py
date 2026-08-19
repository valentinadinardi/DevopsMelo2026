import routeros_api
import os;
# Conectar al router
connection = routeros_api.RouterOsApiPool('192.168.88.1', 'admin', 'admin', '8728', plaintext_login=True)
api = connection.get_api()

# Obtener las interfaces del router
list_interfaces = api.get_resource('interface')
interfaces = list_interfaces.get()
system_resource = api.get_resource('/system/resource')
system_info = system_resource.get()

for interfaz in interfaces:
    print(interfaz['name'], interfaz['running'])
    
cpu = system_info[0]['cpu-load']

print("\n----- MONITOREO DEL SISTEMA -----")
for info in system_info:
    print(f"Uso de CPU: {info.get('cpu-load')}%")
    print(f"Disco libre: {info.get('free-hdd-space')} bytes libres")
    print(f"Memoria Total: {info.get('total-memory')} bytes")
    print(f"Memoria Libre: {info.get('free-memory')} bytes")
    print(f"Versión RouterOS: {info.get('version')}")
    print(f"Uptime: {info.get('uptime')}")

# Cerrar la conexión
connection.disconnect()
