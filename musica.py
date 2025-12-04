"""
Tienes una lista de canciones llamada playlist. Quieres simular el botón de "Siguiente canción".

Lista: playlist = ["Canción 1", "Canción 2", "Canción 3"].

Crea un iterador a partir de esa lista y guárdalo en una variable llamada cola_reproduccion.

Imprime "Reproduciendo: [canción]" usando next() dos veces (para simular que escuchas las dos primeras).

Imprime "Siguiente en la lista: [canción]" usando next() una tercera vez.

Pista: No necesitas bucles (for o while) aquí, el profesor quiere ver que sabes llamar a next() manualmente línea por línea.
"""
def siguiente_cancion():
    playlist = ["Canción 1", "Canción 2", "Canción 3"]

    cola_reproduccion = iter(playlist)

    print(f"Reproduciendo {next(cola_reproduccion)}")
    print(f"Reproduciendo {next(cola_reproduccion)}")
    print(f"Ultima cancion: {next(cola_reproduccion)}")


siguiente_cancion()