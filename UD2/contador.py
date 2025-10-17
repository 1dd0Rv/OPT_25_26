contador = 0


def incrementar():
    global contador
    contador += 1


def decrementar():
    global contador
    contador -= 1


def mostrar_contador():
    print(contador)


incrementar()
incrementar()
decrementar()
mostrar_contador()
print("Roddy es maricon")
