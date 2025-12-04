"""
Eres el encargado de IT. Tienes una lista de diccionarios, donde cada diccionario es una laptop con id, ram (en GB) y status.

Debes recorrer la lista de laptops.

Si una laptop tiene menos de 16 GB de RAM, debes:

Cambiar su status a "Upgrade Required".

Añadir una nueva clave llamada ticket_creado con valor True.

Si tiene 16 GB o más, cambia su status a "OK".

Imprime la lista completa al final para ver los cambios.
"""

def upgrade_ram():

    inventario = [
        {"id": "L001", "ram": 8, "status": "Checking"},
        {"id": "L002", "ram": 32, "status": "Checking"},
        {"id": "L003", "ram": 4, "status": "Checking"}
    ]

    for laptop in inventario:
        if laptop["ram"] < 16:
            laptop["status"] = "Upgrade Required"
            laptop["Ticket"] = True
        else:
            laptop["status"] = "Ok"

    print("---- Equipo actualizado ----")
    for equipo in inventario:
        print(equipo)

upgrade_ram()