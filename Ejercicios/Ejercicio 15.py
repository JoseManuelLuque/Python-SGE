# 15.Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.
# Un año bisiestoes divisible por 4, pero no por 100. También es divisible por 400

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return "Año Bisiesto"
    else:
        return "Año no Bisiesto"

año = int(input("Ingrese año: "))

print(es_bisiesto(año))
