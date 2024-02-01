# 11.Escribir una funcion sum() y una función multip()
# que sumen y multipliquen respectivamente todos los números de
# una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y
# multip([1,2,3,4]) debería devolver 24

listaNumeros = [1,2,3,4,5,6,7,8,9,10]

def sum(listaNumeros):
    suma = 0
    for numero in listaNumeros:
        suma += numero
    return suma

def multip(listaNumeros):
    multiplicacion = 1
    for numero in listaNumeros:
        multiplicacion *= numero
    return multiplicacion

print("Suma: " + str(sum(listaNumeros)))
print("Multiplicacion: " + str(multip(listaNumeros)))