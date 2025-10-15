def registrar_usuario(nombre, edad, ciudad="Madrid"):
    """
    Muestra la informacion del nombre, edad y ciudad de un usuario

    Parametros:
    nombre = str
    edad = int
    ciudad = str
    """
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

registrar_usuario("Roddy", 24, "Huelva")
registrar_usuario("Lucia", 30)
registrar_usuario(nombre="Paco", edad=35)
