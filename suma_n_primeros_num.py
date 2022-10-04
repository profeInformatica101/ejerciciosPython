# Devolver la suma de los diez primeros números
# naturales
'''num = 0
index = 0

while(index <= 10):
    num += index
    index += 1

print("El total es: ", num)
'''
# Devolver la suma de los n primeros
# números naturales
def suma_total(n):
    contador = 0
    acumulador = 0
    while(contador < n):
        contador += 1
        acumulador += contador
    return acumulador
   
    
num = int(input("Dime un número: "))
print("El total de los ", num, " primeros números es ",suma_total(num))
