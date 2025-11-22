"""Recorrer varias listas de estudiantes y sus notas usando enumerate(),
calcular promedios y asignar calificaciones, mostrando todo en un reporte completo con índices.
"""

estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]
resultado_final = {}

for est, mat, fis, qui, in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):
    promedio = round((mat + fis + qui) / 3,2)

    # Variable estado que va a definir si estas aprobados, en recuperacion o reaprobado
    # con control de fujo if, elif
    estado = ""
    if promedio >= 6.5 :
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
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
for i, est in enumerate(resultado_final, start=1):
    datos = resultado_final[est]
    print(
        f"{i} - {est} "
        f"Matemáticas: {datos['Matemáticas']}, "
        f"Física: {datos['Física']}, "
        f"Química: {datos['Química']}, "
        f"Promedio: {datos['Promedio']}, "
        f"Estado: {datos['Estado']}"
        
    )
