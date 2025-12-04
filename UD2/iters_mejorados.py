"""
Contexto: El sistema operativo necesita asignar identificadores de proceso (PIDs). Tienes un rango de PIDs disponibles del 1000 al 1005.

Crea una variable rango_pids usando range(1000, 1005).

Convierte ese rango en un iterador llamado generador_pids.

Crea un bucle infinito while True.

En cada vuelta, intenta obtener el siguiente PID usando next() con un valor por defecto -1 (para indicar error/fin).

Si recibes un PID válido, imprime "Asignando proceso: [PID]".

Si recibes -1, imprime "No hay más PIDs libres" y rompe el bucle.
"""
def asignar_procesos():
    rango_pids = range(1000-1006)

    generados_pids = iter(rango_pids)

    while True:
        pid_actual = next(generados_pids, -1)

        if pid_actual == -1:
            print("Error: No hay mas pids disponibles")
            break
        else:
            print(f"Asignando procesos: {pid_actual}")


asignar_procesos()