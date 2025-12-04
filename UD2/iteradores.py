"""
Tienes una tupla de tareas críticas: tareas = ("Backup DB", "Compilar Kernel", "Desplegar App").

Convierte esa tupla en un iterador explícito.

Usa un bucle while infinito (while True).

Dentro del bucle, usa next() para obtener la siguiente tarea. IMPORTANTE: Debes usar el segundo parámetro de next para devolver None cuando no queden tareas.

Si next devuelve None, rompe el bucle (break) e imprime "Todas las tareas finalizadas".

Si hay tarea, imprime "Procesando: [tarea]...".
"""



def procesar_tareas():
    tareas = ("Backup DB", "Compilar Kernel", "Desplegar App")

    # 1. Crear el iterador explicito
    iterador_tareas = iter(tareas)

    print("--- INICIAND PROCESADOR ---")

    while True:
    # 2. Usar el iterador de forma segura

        tarea_actual = next(iterador_tareas, None)

        if tarea_actual is None:
            print("[!] No quedan tareas, descansa un rato....")
            break

        print(f"Ejecutando: {tarea_actual}...")

procesar_tareas()
