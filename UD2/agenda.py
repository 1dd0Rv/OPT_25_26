"""
Programa de gestion de contactos.

Este programa pide al usuario 3 contactos que los guardara en una agenda creada anteriormenete.
Cada contacto tiene un nombre(Clave) y un telefono(Valor)
Después de meter el contacto se muestra la agenda completa
al final del programa se le da la opcion al usuario de buscar un contacto que se haya guardado anteriormete en la agenda


"""

# Creamos un diccionario vacio en el que meteremos los contactos
agenda = {}
contactos = 0

print(f"\nIntroduce {contactos} contactos para la agenda\n")

# Bucle principal para introducir los 3 contactos
while contactos < 3:
    nombre = input(f"Introduce el nombre de tu contacto {contactos + 1}: ")
    if len(nombre) <= 2:
        print(" El nombre debe tener más de dos caracteres.\n")
        continue

    # Bucle para validar el teléfono
    while True:

        telefono = input(f"Introduce el número de teléfono de {nombre}: ")
        if telefono.isdigit() and len(telefono) > 5:
            break
        print(" El teléfono debe tener más de 5 dígitos y solo contener números.\n")

    # Guardamo el nombre con su valor que sera el telefono
    agenda[nombre] = telefono
    contactos += 1
    print(f"El contacto '{nombre}' se ha guardado correctamente.\n")

print("--- Agenda completa ---")
for nombre, telefono in agenda.items():
    print(f"Nombre: {nombre}, Telefono: {telefono}")

buscar_contacto = input("¿Que contacto quieres buscar?: ")

if buscar_contacto in agenda:
    print(f" Telefono -> {agenda[buscar_contacto]}")
else:
    print(f"El contacto {buscar_contacto} no existe")
