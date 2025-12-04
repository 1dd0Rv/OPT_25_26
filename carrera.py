"""
Imagina que ha terminado una carrera y tienes la lista de llegada de los corredores en orden.

La lista es: corredores = ["María", "Carlos", "Elena", "Roberto"].

Tu tarea es recorrer esa lista usando enumerate.

Debes imprimir en pantalla la posición y el nombre, pero la posición debe empezar en 1 (para que sea "1. María" y no "0. María").

Formato de salida esperado: Posición 1: María, Posición 2: Carlos, etc.

Pista: Recuerda que enumerate acepta un segundo "ingrediente" (argumento) para decirle dónde empezar a contar.
"""

def ordenar_corredores():
    corredores = ["María", "Carlos", "Elena", "Roberto"]

    for i, corr in enumerate(corredores, start=1):
        print(f"Posicion {i}: {corr}")


ordenar_corredores()