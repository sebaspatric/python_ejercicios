"""
script que diga si es hora de ir a casa.
importar modulo time
fecha del sistema
comprobar la hora
si son las 7 mostrar mensaje
caso contrario calcular tiempo que queda de trabajo
"""

import time

hora = time.localtime()
print(hora)
#print(hora.tm_hour)
horaSalida = 7
if hora.tm_hour >= horaSalida:
    print("Es hora de ir a casa")
else:
    texto1 = ("No es hora de ir a casa. La hora de salida es {} hrs\nson las {}:{}".format(horaSalida, hora.tm_hour, hora.tm_min))
    print(texto1)
    horas = (horaSalida-1) - hora.tm_hour
    minutos = 60 - hora.tm_min
    texto2 = "quedan {} horas {} minutos para salir".format(horas, minutos)
    print(texto2)
    #print(hora.tm_min)
print("-------------------")
horaSalida = 19
if hora.tm_hour >= horaSalida :
    print("Es hora de ir a casa")
else:
    texto1 = ("No es hora de ir a casa. La hora de salida es {} hrs\nson las {}:{}".format(horaSalida, hora.tm_hour, hora.tm_min))
    print(texto1)
    horas = (horaSalida-1) - hora.tm_hour
    minutos = 60 - hora.tm_min
    texto2 = "quedan {} horas {} minutos para salir".format(horas, minutos)
    print(texto2)
    #print(hora.tm_min)