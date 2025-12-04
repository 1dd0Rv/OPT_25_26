"""
Tienes una función que recibe un diccionario de un empleado.
 empleado = {"nombre": "Ana", "bruto": 2000}.

Calcula el impuestos (el 10% del bruto). Pista: bruto * 0.10.

Calcula el neto (bruto menos impuestos).

Añade una clave "neto" al diccionario con ese valor final.

Importante: La función debe tener un return que devuelva el diccionario modificado.

Fuera de la función, llama a la función, guarda el resultado en una variable llamada resultado_final e imprímela.
"""
empleado = {"nombre": "Ana", "bruto": 2000}

def calcular_salario(datos_empleado):

    impuesto = datos_empleado["bruto"] * 0.10

    neto = datos_empleado["bruto"] - impuesto

    empleado["neto"] = neto

    return empleado


resultado_final = calcular_salario(empleado)


print(resultado_final)