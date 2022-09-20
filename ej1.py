# Introduciendo la hora del día en horas, minutos y segundos, calcular
# cuantos segundos han transcurrido desde el comiendo del día

#Definir las entradas
hora = 0
minutos = 0
segundos = 0

# Pedir al usuario que ingrese la hora, segundo y minutos actual
hora = int(input("Dime la hora: "))
minutos = int(input("Dime los minutos: "))
segundos = int(input("Dime los segundos: "))

# Realizamos la operación
hora = hora * 3600
minutos = minutos * 60
segundos = segundos + minutos + hora

# Mostramos el resultados
print("Han trascurrido desde el inicio del día ", segundos, " segundos.")