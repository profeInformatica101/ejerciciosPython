# Escriba, usando comparaciones, un algoritmo
# que muestre el estado del agua (hielo, liquido, vapor)
# en función de su temperatura

#inicializamos la temperatura
temp = 0.0

temp = float(input("Dime la temperatura:"))

# Comprobamos los estados
if (temp < 0):
    print(temp, " es HIELO")
else:
    if(temp >= 100):
        print(temp, " es VAPOR")
    else:
        print(temp, " es LÍQUIDO")