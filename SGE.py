def Ejercicio1():
    x = "Buenas Tardes"
    # Usar el método len para imprimir su longitud
    print("La longitud de la cadena es: " + len(x).__str__())

    # Obtener su primer carácter
    print("Su primer caracter es: " + x[0])

    # Obtener los caracteres de la posición 3 a la 6 (no incluido)
    print("Caracteres del 3 al 6:" + x[2:6])


def Ejercicio2():
    x = " Bienvenidos a crase "

    # Devolver la cadena sin los espacios en blanco del principio y final
    print("Cadena sin espacios: " + "'" + x.strip() + "'")

    # Reemplazar el carácter r por l
    print("Cadena remplazada: " + x.replace('r', 'l'))


def Ejercicio3():
    Frutas = ["manzana", "plantano", "fresa"]

    # Imprimir el segundo ítem
    print(Frutas[1])

    # Comprobar si “patata” está en la lista en caso negativo imprime mensaje indicando que patata no es una fruta
    if "patata" not in Frutas:
        print("La patata no es una fruta")

    # Cambiar el valor de “manzana” por “kiwi”
    Frutas[0] = "kiwi"
    print(Frutas)

    # Usar el método append() para añadir a la lista la “naranja”
    Frutas.append("naranja")
    print(Frutas)

    # Usar el método insert() para añadir el limón en el tercer puesto de la lista
    Frutas.insert(2, "limon")
    print(Frutas)

    # Usar el método remove() para eliminar la “fresa”
    Frutas.remove("fresa")
    print(Frutas)

    # Imprimir los ítems de la lista usando un bucle
    for fruta in Frutas: print(fruta)


def Ejercicio4():
    Coche = {"marca": "Ford", "modelo": "Mustang"}

    # Usar el método get para imprimir el valor de la clave “modelo”
    print(Coche.get("modelo"))

    # Añadir la clave/valor: “color” : “rojo” al diccionario de coche
    Coche["color"] = "rojo"
    print(Coche)


# 5. Dados dos números a y b, imprimir “Hola” si a es mayor que b y “Adiós” si a es menor que b
def Ejercicio5():
    a = int(input("Numero A: "))
    b = int(input("Numero B: "))

    if (a>b):
        print("Hola")
    else:
        print("Adios")


# 6. Imprimir los 6 primeros números enteros
def Ejercicio6():
    for i in range(1, 7):
        print(i)

# 7. Dado un número indicar si es par o impar
def Ejercicio7():
    numero = int(input("Numero impar o par: "))

    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")


# 8. Imprimir los números impares desde el 50 hasta la unidad y calcular su suma
def Ejercicio8():
    suma = 0

    for numero in range(49, 0, -2):
        print(numero)
        suma += numero

    print("La suma de los números impares es: " + suma.__str__())


# 9. Calcular el factorial de un número
# def Ejercicio9():

if __name__ == '__main__':
    Ejercicio8()

