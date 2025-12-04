"""
Vamos a simular un semáforo paso a paso.

Tienes una tupla: colores = ("Rojo", "Amarillo", "Verde").

Crea un iterador a partir de esa tupla.

Usa la función next() tres veces seguidas para imprimir cada color manualmente.

Intenta hacer un cuarto next() pero proporcionando un valor por defecto que sea "Semáforo apagado" para que no dé error.

Imprime ese último valor también.

Objetivo: Entender cómo next avanza uno a uno y cómo evitar el error cuando se acaban los datos.
"""

def semaforo():
    colores = ("Rojo", "Amarillo", "Verde")

    iter_colores = iter(colores)

    siguiente_color = (next(iter_colores), None)

    if siguiente_color is None:
        print("Semaforo apagado")
    else:
        print(colores)

semaforo()