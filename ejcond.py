# Realizar un programa que dado
# un número entero diga si es PAR o IMPAR

#inicializamos
num = 0

print("Dime un número: ")
num = int(input())

if (num % 2 == 0):
    print(num, " es un número PAR")
else:
    print(num, " es un número IMPAR")