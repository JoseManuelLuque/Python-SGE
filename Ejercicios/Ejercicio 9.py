# 9. Calcular el factorial de un número

#numero = int(input("Factorial de: "))

# Función recursiva para calcular el factorial de un número
def factorial_recursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

# Ejemplo de uso
factorial = int(input("Factorial de: "))
resultado = factorial_recursivo(factorial)
print("El factorial de " + {factorial} + " es: " + {resultado})
