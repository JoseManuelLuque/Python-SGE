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
