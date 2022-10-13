import random
'''
Estructura secuencial
'''

numaleatorio = random.randint(0,100)

num1 = int(input("Dime un número: "))
if(num1 == numaleatorio):
    print("Has ganado")
else:
    num2 == int(input("Dime otro número:"))
    if(num2 == numaleatorio):
        print("Has ganado")
    else:
        num3 == int(input("Dime otro número:"))
        if(num3 == numaletorio):
            print("Has ganado")
        else:
            print("Has perdido")



'''
Estructura iterativa
'''

numAleatorio = random.randint(0,100)
vidas = 20
print(numAleatorio)
while(vidas > 0):
    numUsuario = int(input("Dime un número: "))
    if(numUsuario != numAleatorio):
        vidas = vidas - 1
        
        if(vidas != 1):
            print("Te quedan ", vidas, " oportunidades.")
        else:
            print("Te quedan ", vidas, " oportunidad.")
        
    else:
        print("Has acertado el número.")
        break
if(vidas == 0):
    print("El número era ", numAleatorio)
    
