'''
Realizar un programa que
calcule el Factorial de un
número
'''
def factorial(n):
    # Inicializo las variables
    index = n
    res = 1
    
    #
    while(index > 0):
        res = res * index
        index -= 1
    
    return res

n = int(input("Dime un número: "))
print("El factorial del número ", n, " es ", factorial(n))

