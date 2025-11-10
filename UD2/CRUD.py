people = {}  # Main dictionary: {nif: {name, age, city, profession}}


def create_person():
    """Create a new person and add to the dictionary."""
    nif = input("Introduce tu DNI: ")

    people[nif] = {
        "name": input("Introduce tu nombre: "),
        "age": input("Introduce tu edad: "),
        "city": input("Introduce tu ciudad: "),
        "profession": input("Introduce tu trabajo: ")
    }


def read_people():
    """Display all registered people."""
    nif = input("Introduce el DNI de la persona que quieres buscar: ")

    if nif in people:
        print(people[nif])
    else:
        print("El usuario no esta registrado")


def update_person():
    """Update information of an existing person."""
    nif = input("Introduce el DNI a actualizar: ")
    if nif in people:
        dato_key = input("Introduce el dato a cambiar (name, age, city, profession): ")
        dato_valor = input("Introduce el nuevo valor: ")

        people[nif].update({dato_key: dato_valor})
    else:
        print(f"{nif} no encontrado")


def delete_person():
    """Delete a person by ID."""
    nif = input("Introduce el DNI a eliminar: ")

    people.pop(nif)


# 🔸 Main menu
option = ""

while option != "5":
    print("\n=== PEOPLE CRUD MENU ===")
    print("1. Create person")
    print("2. Read people")
    print("3. Update person")
    print("4. Delete person")
    print("5. Exit")

    option = input("Choose an option: ")

    match option:
        case "1":
            create_person()
        case "2":
            id = "5"
            lista = []
            while id != "5":
                buscar_dni = input("Introduce el dni que quieras buscar:").split()
                if buscar_dni != 1:
                    lista.append(buscar_dni)
                read_people()
        case "3":
            update_person()
        case "4":
            delete_person()
        case "5":
            print("Exiting program...")
        case _:
            print("Invalid option. Please choose 1–5.")
