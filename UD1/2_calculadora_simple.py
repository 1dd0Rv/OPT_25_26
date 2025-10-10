
num1 = float(input("Pon tu primer número: "))
operator = input("Elige que operador vas a usar (+, -, *, /, %, **): ")
num2 = float(input("Pon tu segundo número"))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "**":
    result = num1 ** num2
elif operator == "%":
        result = num1 % num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:  result = "No se puede dividir entre 0"
else:  result = "No es un operador válido"

#Mostrar resultado
print("El resultado de la operación es: ", result)


