#https://ellibrodepython.com/tiempo-ejecucion-python

import time

'''###############
    Función factorial recursiva while
############
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
'''###############
    Función factorial recursiva for
############
'''
def factorial_for(n):
    res = 1
    
    for i in range(1,n+1):
        res = res * i
    return res


'''###############
    Función factorial Recursiva
############
'''

def factorial_rec(n):
    if(n == 0):
        return 1
    elif(n == 1):
        return 1
    else:
        return n * factorial_rec(n-1)

###########################
# EJECUCIÓN
#########################
N = 30


# guardo en una variable el tiempo actual (El formato es 'the epoch' que comienza dedsde January 1, 1970, 00:00:00 (UTC).) 
inicio = time.time()
#Ejecuto 5 segundos
time.sleep(5)
#print(factorial(30))
fin = time.time()
total = fin - inicio
print("Ejecución programa que duerme 5 segundos - total: ", total , " segundos." )


print(" ---- FUNCIONES FACTORIAL --- para n = ", N)
inicio = time.time()
factorial_while(N)
fin = time.time()
total = fin - inicio
print("Ejecución programa FACTORIAL WHILE: ", total , " segundos." )

inicio = time.time()
factorial_for(N)
fin = time.time()
total = fin - inicio
print("Ejecución programa FACTORIAL FOR: ", total , " segundos." )

inicio = time.time()
factorial_rec(N)
fin = time.time()
total = fin - inicio
print("Ejecución programa FACTORIAL RECURSIVO: ", total , " segundos." )

