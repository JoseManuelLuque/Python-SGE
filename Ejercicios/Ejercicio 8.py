# 8. Imprimir los números impares desde el 50 hasta la unidad y calcular su suma

suma = 0

for numero in range(49, 0, -2):
    print(numero)
    suma += numero

print("La suma de los números impares es: " + suma.__str__())
