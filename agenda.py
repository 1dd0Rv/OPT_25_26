agenda = {}
contactos = 3

print(f"\nIntroduce {contactos} contactos para la agenda\n")

# Bucle principal para introducir los 3 contactos
for i in range(contactos):
    while True:
        nombre = input(f"Introduce el nombre de tu contacto {i + 1}: ")
        if len(nombre) > 2:
            break
        print(" El nombre debe tener más de dos caracteres.\n")

    # Bucle para validar el teléfono
    while True:
        telefono = input(f"Introduce el número de teléfono de {nombre}: ")
        if telefono.isdigit() and len(telefono) > 5:
            break
        print(" El teléfono debe tener más de 5 dígitos y solo contener números.\n")

    # Guardamo el nombre con su valor que sera el telefono
    agenda[nombre] = telefono
    print(f"El contacto '{nombre}' se ha guardado correctamente.\n")

print("--- Agenda completa ---")
print(agenda)

buscar_contacto = input("¿Que contacto quieres buscar?: ")

if buscar_contacto in agenda:
    print(f" Telefono -> {agenda[buscar_contacto]}")
else:
    print(f"El contacto {buscar_contacto} no existe")
