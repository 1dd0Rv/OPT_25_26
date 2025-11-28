"""Tenemos un diccionario con estudiantes y sus notas en tres materias:
Crea un iterador sobre las claves del diccionario.

Recorre el iterador usando next() dentro de un while True.

Para cada estudiante:

Calcula el promedio de sus notas.

Determina el estado:

"Aprobado" si promedio ≥ 6.5
"En recuperación" si promedio ≥ 5 y < 6.5
"Reprobado" si promedio < 5
Imprime un reporte claro y ordenado:
"""


def promedio(notas):
    return sum(notas) / len(notas)

def estado_notas(promedio):
    if promedio >= 6.5 :
        return "Aprobado"
    elif promedio >= 5:
        return "En recuperación"
    else:
        return "Reaprobado"

estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}

it = iter(estudiantes)

while True:
    try:
        # Obtiene la siguiente clave (nombre del estudiante) del iterador
        estudiante_nombre = next(it)

        notas_estudiante = estudiantes[estudiante_nombre]
        promedio_final = promedio(notas_estudiante)

        estado = estado_notas(promedio_final)

        print(f"[!] Estudiante: {estudiante_nombre}")
        print(f"   - Notas: {notas_estudiante}")
        print(f"   - Promedio: {promedio_final:.2f}")
        print(f"   - Estado: **{estado}**")
        print("-" * 30) # Separador entre estudiantes

    except StopIteration:

        break
