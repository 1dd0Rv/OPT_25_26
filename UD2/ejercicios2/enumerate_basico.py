"""
Tienes una lista de productos para comprar. El profesor quiere que generes una lista nueva donde cada elemento sea un string que diga "Artículo N: Nombre".

La lista original es: productos = ["Pan", "Leche", "Huevos", "Arroz"].

Usa enumerate para recorrerla.

La numeración debe empezar en 1 (no en 0).

Guarda el resultado en una lista llamada lista_formateada.

Imprime esa lista final.
"""
def lista_compra():
    productos = ["Pan", "Leche", "Huevos", "Arroz"]
    lista_formateada = []

    for i, compra in enumerate(productos, start=1):
        texto = print(f"Articulo {i}, {compra}")
        lista_formateada.append(texto)
    print(lista_formateada)


lista_compra()
