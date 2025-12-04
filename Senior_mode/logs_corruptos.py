"""
Recibes una lista de logs "sucios" de un servidor. Cada cadena tiene el formato "ID_USER:ACCION:TIEMPO". Tu misión es limpiar esto y generar una lista de diccionarios estructurada,
pero solo de los usuarios que tardaron más de 500ms.

Datos de entrada: logs = ["u1:login:120", "u2:upload:800", "u1:logout:30", "u3:backup:6000", "u2:login:50"]

Requisitos:

Usa enumerate empezando por el ID de evento 5000.

Debes separar la cadena de texto para obtener los datos (investiga o recuerda cómo separar un string por los dos puntos :).

Tienes que convertir el tiempo a número entero para poder compararlo.

Genera una lista alertas que contenga diccionarios con este formato exacto: {'id_evento': 5000, 'usuario': 'u2', 'mensaje': 'ALERTA: upload tardó 800ms'}

Output esperado: Una lista con 2 diccionarios (el de u2 y el de u3).

Pista SysAdmin: El metodo .split(":") convierte un string en una lista de trozos.
"""

logs = ["u1:login:120", "u2:upload:800", "u1:logout:30", "u3:backup:6000", "u2:login:50"]

def clear_log():
    # Lista de alertas
    alerta = []

    #Enumerate como pide el enunciado
    for id_evento, log in enumerate(logs, start=5000):
        user, accion, ms= log.split(":")
        ms = int(ms)
        if ms > 500:
            evento = {
                    "id_evento": id_evento,
                    "usuario": user,
                    "ALERTA": f"{accion} tardó {ms}ms"
                    }
            alerta.append(evento)
    return alerta

log_procesados = clear_log()

print("-----Logs criticos-------")
for log in log_procesados:
    print(log)

