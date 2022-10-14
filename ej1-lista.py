import random

def listavacia():
    lst = []
    return lst
'''
Definir una función que devuelva una
lista con 20 números random
'''
# lista_numeros()
# devuelve por ejemplo ---> [2,4,3,4,5,17,3,4,7,9,10,12,15,16,18,29,98,87, 65, 30]
# len(lista_numeros()) --> 20
# type(lista_numeros()) --> <class 'list'>
def lista_numeros():
    pass
    
def lista_numeros_for():
    lst = []
    for i in range(0,20):
        lst.append(random.randint(0,100))
    return lst

def lista_numeros_while():
    lst = []
    contador = 0
    while(contador < 20):
        numeroRandom = random.randint(0,100)
        contador += 1
        lst.append(numeroRandom)
        
    return lst
'''
Definir una función que dado una lista
filtre los números pares
'''
# filtra_lista_pares([1,2,3,4])
# devuelve ---> [2,4]
def filtra_lista_pares(lst):
    #crear una nueva lista vacia que se llame pares
    lst_pares = []
    #recorrer con un for todos los elementos de lst
    for i in lst:
        # si cada elemento en cada iteracion es par
        if(i % 2 == 0):
           # añadirlo a la nueva lista (pares)
           lst_pares.append(i)
    # devolver la nueva lista (pares)
    return lst_pares
  

lst_test = lista_numeros_for()
print(lst_test)
print(filtra_lista_pares(lst_test))
'''
Definir una función que dado una lista y un número
devuelva
   - True si se encuentra el número en la lista
   - False e.c.c.
'''
def busquda_num(lst, num):
    pass
