"""
Tienes una "base de datos" (una lista de diccionarios) con usuarios.

Debes crear una función guardar_usuario que reciba la lista, un email (clave única), nombre y rol.

Si el usuario con ese email ya existe en la lista, actualiza su nombre y rol.

Si el usuario no existe, crea un nuevo diccionario y añádelo a la lista.

La función no debe devolver nada, modifica la lista in-place (por referencia).

"""

# --- Programa Principal ---
db_usuarios = [
    {"email": "admin@sys.com", "nombre": "Admin", "rol": "SuperUser"},
    {"email": "pepe@sys.com", "nombre": "Pepe", "rol": "User"}
]

def guardar_usuario(lista_db, email, nombre, rol):
    """
    Realiza un Upsert: Actualiza si existe, Inserta si no.
    """
    usuario_encontrado = False

    # 1. Buscamos si existe (Recorrido secuencial)
    for usuario in lista_db:
        # Accedemos por clave
        if usuario["email"] == email:
            # UPDATE: Modificamos el diccionario existente
            usuario["nombre"] = nombre
            usuario["rol"] = rol
            usuario_encontrado = True
            print(f"[UPDATE] Usuario {email} actualizado.")
            break # dejarmos de buscar si ya lo encontramos

    # 2. Si terminamos el bucle y no estaba, insertamos
    if not usuario_encontrado:
        # CREATE: Creamos el diccionario nuevo [cite: 589]
        nuevo_usuario = {"email": email, "nombre": nombre, "rol": rol}
        lista_db.append(nuevo_usuario) # [cite: 435]
        print(f"[INSERT] Usuario {email} creado.")

# Caso 1: Insertar uno nuevo
guardar_usuario(db_usuarios, "juan@sys.com", "Juan", "Dev")

# Caso 2: Actualizar uno existente
guardar_usuario(db_usuarios, "admin@sys.com", "Administrator", "GodUser")
guardar_usuario(db_usuarios, "roddy@proton.es", "Hack4u", "PWNED")

print("\n--- ESTADO FINAL DB ---")
for u in db_usuarios:
    print(u)




