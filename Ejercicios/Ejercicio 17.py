# 17.Realizar una calculadora:
# Se solicita la introducción de los dos operandos y el operador por teclado
# Se muestra el resultado de la operación de tal forma:
# “La operación es:    ““El resultado es      “

operando1 = int(input("Ingrese numero 1: "))
operando2 = int(input("Ingrese numero 2: "))
operador = input("Ingrese Operador: \n s: Sumar \n r: Restar \n m: Multiplicar \n d: Dividir \nOperador: ")

print("")

if operador == "s":
    print(operando1 + operando2)
if operador == "r":
    print(operando1 - operando2)
if operador == "d":
    print(operando1 / operando2)
if operador == "m":
    print(operando1 * operando2)
else:
    print("Errorr")