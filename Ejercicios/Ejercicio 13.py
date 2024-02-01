# 13.Escribir una función mas_larga() que tome una lista de palabras y devuelva la máslarga

listaPalabras = ["hola", "adios", "walalulu", "a"]

def mas_larga(listaPalabras):
    palabra_mas_larga = listaPalabras[0]

    for palabra in listaPalabras[1:]:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga

print(mas_larga(listaPalabras))