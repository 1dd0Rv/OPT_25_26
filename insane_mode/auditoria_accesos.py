"""
Eres el administrador de seguridad. Tienes una lista de intentos de acceso a un servidor.

Datos: intentos = ["Admin", "User1", "Hacker", "User2", "Hacker", "Admin"].

Debes detectar a los intrusos ("Hacker").

Usa enumerate para recorrer la lista, pero simulando que las líneas del log empiezan en la 100 (param start).

Crea una lista llamada reporte_seguridad.

Si encuentras un "Hacker", guarda en la lista una tupla con este formato: (Numero_Linea, "ALERTA: Intruso detectado").

Si es un usuario normal, no guardes nada.

Al final, imprime la lista de reportes.

"""
def impostor():
    intentos = ["Admin", "User1", "Hacker", "User2", "Hacker", "Admin"]

    reporte_seguridad =[]

    for id, user in enumerate(intentos, start=100):
        if user == "Hacker":
            reporte_seguridad.append((f"{id}, ALERTA: INTRUSO DETECTADO {user}"))
    print(reporte_seguridad)


impostor()