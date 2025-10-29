nombres = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]

for n, m, f in zip(nombres, notas_matematicas, notas_fisica):
    print(f"{n} - Matematicas: {m}, Física: {f}")