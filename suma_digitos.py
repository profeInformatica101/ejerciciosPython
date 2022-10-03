# Introducir un número y devolver la suma de sus dígitos
'''
Ejemplo la función suma_digitos(234)
                         devolvería 9
                         
'''

#--------------------------
#     Solucion 1: Con tipo de dato String
#--------------------------
def suma_digito(numero):
    resultado = 0
    str_numero = str(numero)
    
    for i in str_numero:
        resultado += int(i)
 
    return resultado

#print(suma_digito(234))

#--------------------------
#     Solucion 2: Con tipo de dato Entero
#--------------------------

def suma_digito2(numero):
    print("sumadigito2")
    resultado = 0
    
    while(numero >= 10):
        resultado += (numero % 10)
        numero = (numero // 10)
    resultado += numero
    return resultado

print(suma_digito2(234))
