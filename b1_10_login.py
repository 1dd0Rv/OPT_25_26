save_user = []
save_password = []

option = ""

while option != "3":
    option = input("\nBienvenido al menú principal de roddy.com\n"
                   "1) Registrarse\n"
                   "2) Iniciar sesión\n"
                   "3) Salir\n"
                   "Seleccione una opción: ")

    # OPCIÓN 1: REGISTRARSE

    if option == "1":
        print("\n--- REGISTRO ---")

        # Validación del usuario (email)
        while True:
            user = input("Introduce tu email: ")

            if (len(user) < 3 or
                    "@" not in user or
                    not (user.endswith(".com") or user.endswith(".es") or user.endswith(".net")) or
                    any(c in "!#$%&*?;:/<>^{}[]" for c in user)):  # símbolos prohibidos
                print(
                    "El email debe tener mínimo 3 caracteres, contener '@', acabar en (.com, .es, .net) y no tener símbolos especiales.")
                continue

            if user in save_user:
                print("Ese usuario ya está registrado. Intenta con otro.")
                continue

            break

        # Validación de la contraseña
        while True:
            password = input("Introduce una contraseña: ")

            if (len(password) < 8 or
                    not any(c.isupper() for c in password) or
                    not any(c.isdigit() for c in password) or
                    not any(c in "!@#$%&*?;" for c in password)):
                print(
                    "La contraseña debe tener mínimo 8 caracteres, una mayúscula, un número y un símbolo especial (!@#$%&*?;).")
                continue
            break

        # Guardar usuario y contraseña
        save_user.append(user)
        save_password.append(password)
        print(f"\n{user} se ha registrado correctamente.\n")


    # OPCIÓN 2: INICIAR SESIÓN

    elif option == "2":
        print("\n--- INICIAR SESIÓN ---")

        login_exitoso = False

        # Bucle para permitir volver a intentar si el usuario no existe
        while not login_exitoso:
            login_user = input("Introduce tu email (o escribe '3' para volver al menú): ")

            if login_user == "3":
                print("Regresando al menú principal...\n")
                break

            if login_user in save_user:
                index = save_user.index(login_user)
                intentos_login = 0
                limite_login = 3

                while intentos_login < limite_login and not login_exitoso:
                    login_passwd = input("Introduce tu contraseña: ")

                    if login_passwd == save_password[index]:
                        print("✅ Acceso concedido.")
                        login_exitoso = True
                    else:
                        intentos_login += 1
                        if intentos_login < limite_login:
                            intentos_restantes = limite_login - intentos_login
                            print(f"⛔ Contraseña incorrecta. Te quedan {intentos_restantes} intentos.")
                        else:
                            print("🚫 Demasiados intentos fallidos. Regresando al menú principal.")
                if login_exitoso:
                    print("Has iniciado sesón correctamente")
                break
            else:
                print(
                    f"El usuario '{login_user}' no está registrado. Intenta nuevamente o escribe 'salir' para volver.\n")

    # OPCIÓN 3: SALIR

    elif option == "3":
        print("\n👋 Saliendo del programa... ¡Hasta luego!\n")
    else:
        print("️ Opción no válida. Intente nuevamente.\n")
