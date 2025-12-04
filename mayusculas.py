# crea una funcion formatear nombre
# Devuelve el nombre completo en mayuscula

def formatear_nombre(nombre, apellidos):
    m_nombre = nombre.upper()
    m_apellidos = apellidos.upper()

    return m_nombre, m_apellidos

print(formatear_nombre(nombre="Adrian", apellidos = "Morales"))