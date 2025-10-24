compras = []

print("Vamos a hacer la lista de la compra: \n")
lista_compra = input("Introduce los articulos que necesitas comprar: ")

compras.extend(lista_compra.split())
print(compras)

producto_eliminado = input("Quieres eliminar algun producto de la lista:")
compras.remove(producto_eliminado)

compras.sort()

print(compras)
