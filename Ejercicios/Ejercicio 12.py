# 12.Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
# Por ejemplo: generar_n_caracteres(5,"x") debería devolver "xxxxx"

letra = str(input("Ingrese Letra: "))
numero = int(input("Ingrese Numero: "))

def generarCaracteres(numero, letra):
    resultado = ""
    resultado += numero*letra
    return resultado

print(generarCaracteres(letra, numero))