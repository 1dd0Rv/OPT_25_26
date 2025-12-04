"""
Tienes un diccionario que representa a un alumno con sus notas en una lista. Debes calcular su promedio y actualizar el diccionario.

Datos: alumno = {"nombre": "Luis", "notas": [7, 8, 9], "curso": "Python"}.

Calcula el promedio de las notas (suma de notas dividido por la cantidad).

Añade una nueva clave al diccionario llamada "promedio" con el valor calculado.

Si el promedio es 5 o más, añade otra clave "aprobado" con valor True. Si no, False.

Imprime el diccionario completo al final.

Objetivo: Modificar un diccionario añadiendo claves nuevas basadas en cálculos de sus propios datos.
"""



def promedio():
    alumno = {"nombre": "Luis", "notas": [7, 8, 9], "curso": "Python"}

    lista_notas = alumno["notas"]
    promedio = sum(lista_notas) / len(lista_notas)

    alumno["Promedio"] = promedio

    if promedio >= 5:
        alumno["Aprobado"] = True
    else:
        alumno["Aprobado"] = False

    print(alumno)
    
promedio()