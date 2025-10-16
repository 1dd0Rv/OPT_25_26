def suma(a,b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

option = ""
while option != "5":

    option=input("""===== CALCULADORA =====
    Elije que operacion quieres hacer
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Salir\n""")

    if option == "1":
        a=int(input("Introduce el primer numero: "))
        b=int(input("Introduce el segundo numero: "))
        print("Resultado: ", suma(a,b))

    elif option =="2":
        a=int(input("Introduce el primer numero: "))
        b=int(input("Introduce el segundo numero: "))
        print("Resultado: ", restar(a,b))

    elif option =="3":
        a=int(input("Introduce el primer numero: "))
        b=int(input("Introduce el segundo numero: "))
        print("Resultado: ", multiplicar(a,b))

    elif option == "4":
        a=int(input("Introduce el primer numero: "))
        b=int(input("Introduce el segundo numero: "))
        if b != 0:
            print("Resultado: ", dividir(a,b))

        else:
            print("Math error")

    elif option == "5":
        print("Saliendo de la calculadora...")


    else:
     print("Opcion no valida, intente de nuevo")