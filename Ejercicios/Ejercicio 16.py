# 16.Calcular la letra que corresponde a un dni:
# Se solicita la introducción del DNI por teclado (el formato correcto es una sucesión de 8 números enteros NNNNNNNN)
#
# Si el formato del DNI es correcto se calcula la letra que corresponde  y  se  escribe por pantalla
# “La letra que corresponde al DNI introducido es” X y el NIF completo es NNNNNNNNX
#
# Si el formato del DNI es incorrecto se escribe por pantalla “Formato de DNI incorrecto” y
# se vuelve a solicitar la introducción del DNI

def calcular_letra_dni(numeroDNI):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    try:
        if not (isinstance(numeroDNI, int) and 0 <= numeroDNI <= 99999999):
            raise ValueError("Formato de DNI incorrecto")

        letra = letras[numeroDNI % 23]

        return letra

    except ValueError as error:
        raise ValueError("Error: " + str(error))


while True:
    try:
        DNI = int(input("Introduce el DNI: "))
        print("La letra es: " + calcular_letra_dni(DNI))
        break

    except ValueError as e:
        print("Error: " + str(e) + " Vuelve a introducir el DNI.")
