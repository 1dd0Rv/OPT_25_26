"""
Tienes una lista de mensajes de log de un sistema. Necesitamos extraer solo los mensajes de tipo CRITICAL para enviarlos a un reporte urgente.

La lista es: logs = ["INFO", "WARNING", "CRITICAL", "INFO", "CRITICAL", "DEBUG"].

Las líneas del archivo de log no empiezan en 0, sino en la línea 500 (usa el parámetro start).

Genera una lista llamada reporte que contenga tuplas con el formato: (Numero_Linea, "Mensaje: CRITICAL").

Ojo: En la tupla, el segundo elemento debe ser un string formateado, no solo la palabra "CRITICAL".
"""

def filtrar_logs():

    logs = ["INFO", "WARNING", "CRITICAL", "INFO", "CRITICAL", "DEBUG"]

    reporte = []

    for num_lin, estado in enumerate(logs, start=500):
        if estado == "CRITICAL":
            item = (num_lin, f"Mensaje: {estado}")
            reporte.append(item)
    print(reporte)

filtrar_logs()

