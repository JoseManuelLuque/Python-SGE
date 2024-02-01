# 10. Escribir una función que tome un carácter y
# devuelva True si es una vocal,de lo contrario devuelve False

caracter = str(input("Ingrese un caracter: "))

def comprobarVocal(carcater):
    vocales = ["a", "e", "i", "o", "u"]

    if carcater in vocales:
        return True
    else:
        return False

print(comprobarVocal(caracter))