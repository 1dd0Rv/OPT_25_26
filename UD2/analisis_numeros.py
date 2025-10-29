
"""
Este programa primero generamos una lista con 20 numeros usando un rango

Esta lista la usamos para generas listas y diccionarios qye hagan:
Una lista con los cuadrados de todos los números.
Una lista con solo los números pares.
Una lista con los números mayores que 10.
Cree un diccionario que relacione cada número con su doble.

Todos lso resultados de las listas van a aparecer en pantalla

"""
# Genere una lista de 20 números enteros (pueden ser introducidos manualmente o generados con range)
numeros_generados = [n for n in range(21)]
print(numeros_generados)

# Una lista con los cuadrados de todos los números.
cuadrados_numeros = [ n ** 2 for n in numeros_generados ]
print(cuadrados_numeros)

# Una lista con solo los números pares.
numeros_pares = [n for n in numeros_generados if n % 2 == 0]
print(numeros_pares)

# Una lista con los números mayores que 10.
numeros_mayores = [n for n in numeros_generados if n > 10]
print(numeros_mayores)

# Cree un diccionario que relacione cada número con su doble.
numeros_dobles = {n: n ** 2 for n in numeros_generados}
print(numeros_dobles)