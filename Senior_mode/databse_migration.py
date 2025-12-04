"""
1.  Tienes que mover usuarios de un servidor "Legacy" a un servidor "Cloud".
    Crea una función migrar_usuario(db, nombre_usuario) que reciba la base de datos completa y el nombre.

 2. Lógica de la Función:

- Busca al usuario en base_datos["legacy"].

- Si existe y activo es True:

- Mueve sus datos a base_datos["cloud"] (copia el diccionario).

- Añade una clave nueva al usuario en Cloud: "migrado": True.

- Borra al usuario de la sección "legacy" (comando del o pop).

- Devuelve True.

- Si no existe o no está activo, devuelve False.

3. Reto: Ejecuta la función para "maria", guarda el booleano de resultado, e imprime la base_datos completa al final para ver que María ya no está en legacy y sí en cloud.
"""
base_datos = {
    "legacy": {
        "pepe": {"saldo": 100, "activo": True},
        "maria": {"saldo": 5000, "activo": True}
    },
    "cloud": {}
}







def esta_activo(db, sistema, usuario):
    sistema = sistema.lower()
    usuario = usuario.lower()

    if sistema not in db:
            return False

    if usuario not in db[sistema]:
        return False

    return db[sistema][usuario]["activo"]

    #if esta_activo() == True:



#db = base_datos.keys()
#print(db)

#nombre_usuario =  base_datos.values(),
#print(nombre_usuario)

#usuario_activo = base_datos[nombre_usuario]
#item_usuario = nombre_usuario.items()

#for nom_usu, dinero, actividad in nombre_usuario.items():
    #if actividad == True:



"""def mover_usuario(db, nombre_usuario):
   # db legacy
    db = base_datos.keys()

    #Buscar usuario en la base de datos
    nombre_usuario = base_datos.values()

    for nombre_usuario in base_datos:
        if db["nombre_usuario"]["activo"] = True"""



