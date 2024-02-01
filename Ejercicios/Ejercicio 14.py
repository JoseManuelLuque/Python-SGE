# 14.Escribir un programa que le diga al usuario que ingrese una cadena.
# El programa tiene que evaluar la cadena y decir cuántasletras mayúsculas tiene.

cadena = str(input("Ingrese cadena: "))

contadorMayusculas = 0

for caracter in cadena:
    if caracter.isupper():
        contadorMayusculas += 1

print("La cadena tiene" + str(contadorMayusculas) + "letras mayúsculas.")