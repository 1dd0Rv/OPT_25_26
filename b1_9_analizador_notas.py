lista_notas = [] # Creamos la lista en la que se van a guardar las notas



for i in range(1,4):
    nota = float(input(f"Introduce tus nota {i}: \n"))
    lista_notas.append(nota)

#promedio = sum(lista_notas) / 2 // Calculamos las notas, error logico dividir entre dos, para que el programa sea funcional hay
# que dividir entre el lenght de la lista

promedio = sum(lista_notas) / len(lista_notas)
print(promedio)
