"""
Tienes una lista de estados de servidores. Tu tarea es detectar cuáles han fallado ("ERROR") y guardar sus IDs en una lista de tuplas.

La lista de servidores es: ["OK", "OK", "ERROR", "OK", "ERROR", "MAINTENANCE"].

Los IDs de los servidores no empiezan en 0, sino en 100 (parámetro start de enumerate).

Crea una lista llamada alertas que contenga tuplas con el formato (ID, Estado) solo de los servidores que sean "ERROR".

Imprime la lista final de alertas.
"""

# funcion para los datos hardcodeados

def auditar_servidores():
    # Datos hardcodeados (sin input)
    estados = ["OK", "OK", "ERROR", "OK", "ERROR", "MAINTENANCE"]
    alertas = []

    # Uso de enumerate con start=100 para simular IDs reales
    # iteramos obteniendo indice (id_servidor) y valor (estado)
    for id_servidor, estado in enumerate(estados, start=100):
        # Lógica de filtrado
        if estado == "ERROR":
            # Guardamos como tupla (inmutable y ligera)
            alertas.append((id_servidor, estado))

    print("--- REPORTE DE ALERTAS ---")
    print(alertas)

# Ejecución
auditar_servidores()

