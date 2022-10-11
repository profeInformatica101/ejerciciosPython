# Función esPrimo
# Entrada: (Entero) n
# Salida: (Booleano) resultado
'''
Devuelve si n es Primo o no.
True es primo 
False no es primo
'''
def esPrimo(n):
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

'''3.4. Escriba un algoritmo que proporcione
los números primos comprendidos entre 1 y 1000.
Recuerde que un número primo solo es divisible
entre sí mismo y por la unidad.
Preste atención, lo más sencillo no siempre es lo
más rápido.
'''
def primeros1000primos_for():
    lst = []
    for i in range(1,1001):
        if(esPrimo(i)):
            lst.append(i)
    return lst
  
def primeros1000primos_while():
    i = 1
    lst = []
    
    while(i < 1000):
        if(esPrimo(i)):
            lst.append(i)
        i = i + 1
    return lst

