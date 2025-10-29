"""Crear un diccionario vacío llamado resultado_final.

Usar zip() para recorrer todas las listas al mismo tiempo y calcular:

Promedio de cada estudiante.

Estado final:

Aprobado si promedio ≥ 6.5
En recuperación si promedio ≥ 5 y < 6.5
Reprobado si promedio < 5
Guardar en el diccionario resultado_final de esta forma:"""

estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]
resultado_final = {}

# Recorer listas para ver que notas tienen y calculamos el promedio
# y lo guardamos en una variable

for est, mat, fis, qui, in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):
    promedio = round((mat + fis + qui) / 3,2)

    # Variable estado que va a definir si estas aprobados, en recuperacion o reaprobado
    # con control de fujo if, elif
    estado = ""
    if promedio >= 6.5 :
        estado = "Aprobado"
    elif promedio >= 5 or promedio < 6.5:
        estado = "En recuperacion"
    else:
        estado = "Reaprobado"

    # Metemos las notas, promedio y estado como valor(diccionario)
    # Para la clave (Estudiantes)
    resultado_final[est] = {
        "Matemáticas" : mat,
        "Física" : fis,
        "Química" : qui,
        "Promedio" : promedio,
        "Estado" : estado
    }

# Bucle para mostar ordenadamente toda la lista
print("---- Resultado de las Notas ----")
for est, mat, fis, qui in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):
    datos = resultado_final[est]
    print(
        f"{est} - "
        f"Matemáticas: {datos['Matemáticas']}, "
        f"Física: {datos['Física']}, "
        f"Química: {datos['Química']}, "
        f"Promedio: {datos['Promedio']}, "
        f"Estado: {datos['Estado']}"
    )

