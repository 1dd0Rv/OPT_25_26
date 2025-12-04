"""
Tienes una lista de invitados VIP. El profesor quiere que generes una nueva lista de strings donde cada invitado tenga su número de asiento.

Lista: invitados = ["Lady Gaga", "Messi", "Rosalía"].

Los asientos empiezan en el número 10 (usa start=10).

Crea una lista vacía llamada asientos_asignados.

Recorre la lista con enumerate. En cada vuelta, crea un texto como: "Asiento 10: Lady Gaga" y guárdalo en la lista asientos_asignados (usa append).

Al final, imprime la lista completa.
"""

def aignar_asientos():
    invitados = ["Lady Gaga", "Messi", "Rosalía"]
    asientos_asignados = []

    for asiento, inv in enumerate(invitados, start=10):
        culos = print(f"Asiento {asiento}: {inv}")
        asientos_asignados.append(culos)

    print(asientos_asignados)


aignar_asientos()