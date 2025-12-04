"""
ienes una función actualizar_producto que recibe un diccionario con la info de un producto.

Diccionario de entrada: producto = {"id": "A55", "precio": 10, "stock": 4}.

Lógica dentro de la función:

Calcula el valor total del inventario (precio * stock) y guárdalo en una nueva clave "valor_total".

Si el stock es menor de 5, añade una clave "estado" con valor "PEDIR_RECAMBIO".

Si el stock es 5 o más, la clave "estado" debe ser "OK".

IMPORTANTE: La función debe devolver (return) el diccionario modificado.

Programa principal:

Crea el diccionario.

Llama a la función y atrapa el resultado en una variable producto_procesado.

Imprime producto_procesado.
"""



def gestion_stock(datos_productos):

    valor_total = datos_productos["precio"] * datos_productos["stock"]
    datos_productos["Valor total"] = valor_total

    if datos_productos["stock"] < 5:
        datos_productos["Estado"] = "Pedir_recambio"
    else:
        datos_productos["Estado"] = "ok"

    return datos_productos

producto = {"id": "A55", "precio": 10, "stock": 4}

producto_procesado = gestion_stock(producto)

print(producto_procesado)

