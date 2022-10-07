'''
Realizar un programa que
calcule el Factorial de un
número
'''
def factorial_while(n):
    # Inicializo las variables
    index = n
    res = 1
    
    #
    while(index > 0):
        res = res * index
        index -= 1
    
    return res

def factorial_for(n):
    res = 1
    
    for i in range(1,n+1):
        res = res * i
    return res

n = int(input("Dime un número: "))
print("El factorial del número ", n, " es ", factorial_for(n))

