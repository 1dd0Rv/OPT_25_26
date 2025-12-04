"""
Vas a simular un procesador de tareas que a veces falla.

Tupla de tareas: cola = ("Tarea 1", "Tarea 2", "Tarea 3").

Crea un iterador llamado procesador.

Fase 1 (Manual): Procesa (imprime) la primera tarea usando next().

Fase 2 (Bucle Seguro): Quieres procesar el resto automáticamente hasta que se acaben.

Usa un while True.

Dentro, usa next(procesador, None) para intentar sacar la siguiente tarea.

Si recibes None, imprime "Fin del procesamiento" y rompe el bucle (break).

Si recibes una tarea, imprime "Procesando lote: [tarea]".
"""

def lista_tareas():
    cola = ("Tarea 1", "Tarea 2", "Tarea 3")
    procesador = iter(cola)

    while True:
        siguiente_tarea = next(procesador, None)

        if siguiente_tarea is None:
            print("Fin del procesamiento...")
            break
        else:
            print(f"Procesando lote: {siguiente_tarea}")


lista_tareas()