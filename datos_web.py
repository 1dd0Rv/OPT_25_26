"""
Tienes un diccionario con los datos básicos de un usuario que quiere entrar a un sitio web.

Datos: usuario = {"nick": "Gamer123", "edad": 17, "pais": "España"}.

Debes comprobar si el usuario es mayor de edad (18 años o más).

Si la edad es 18 o más, añade una nueva clave al diccionario: "acceso_permitido": True.

Si es menor de 18, añade la clave: "acceso_permitido": False.

Imprime el diccionario final para ver que se ha añadido la etiqueta de acceso.

Pista: Para añadir algo a un diccionario solo necesitas hacer diccionario["nueva_clave"] = valor.
"""

def control_usuarios():
    usuario = {"nick": "Gamer123", "edad": 17, "pais": "España"}

    edad_usuario = usuario["edad"]

    if edad_usuario <= 17:
        usuario["Acceso permitido"] = False
    else:
        usuario["Acceso permitido"] = True
    print(usuario)

control_usuarios()