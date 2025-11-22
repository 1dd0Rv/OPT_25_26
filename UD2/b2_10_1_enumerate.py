nombres = ["Ana", "Luis", "Marta", "Carlos"]

for indice, nom in enumerate(nombres):
    print(indice, nom)

lista_converted = list(enumerate(nombres))
print(lista_converted)