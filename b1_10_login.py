special_char = '*', '+', '-', '/', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '>', '<', '~', '°', '^', '&', '$', '#', '"'
option = input("Bienvenido al menu principal de roddy.com\n"
               "1) Registrar\n"
               "2) Iniciar sesion\n"
               "3) Salir\n")
while True:
    save_user = []
    save_password = []
    if option == "1":
        user = input("Introduce nombre de usuario: ")
        if (len(user) < 3 or "@" not in user
                or not (user.endswith(".com") or user.endswith(".es") or user.endswith(".net"))
                or any(c in special_char for c in user)):
            print(
                "El usuario debe tener minimo 3 caracteres, no debe tener caracteres especiales y acabar en (.com, .es, .net)")
        else:
            password = input("Introduce una contraseña: ")
            if (len(password) < 8 or
                    not any(c.isupper() for c in password) or
                    not any(c.islower() for c in password) or
                    not any(c in special_char for c in password)):
                print(
                    "La contraseña debe tener mininmo 8 caracteres, una mayuscula una minuscula y un simbolo especial.")
            else:
                save_user.append(user)
                save_password.append(password)

    if option == "2":
        print("Inicia sesion")
