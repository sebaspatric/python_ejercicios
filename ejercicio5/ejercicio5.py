#escriba una funcion para deccir si un año es bisiesto o no
print("-------prueba-------------")

anho = 1600

#if (anho % 4 == 0) and (anho % 100!= 0) or (anho % 400 == 0):
if (anho % 4 == 0) & (anho % 100!= 0) | (anho % 400==0):
    print("Es bisiesto")    

print("\n---------------------------")
def isBisiesto(anho):
    restultadp =  (anho % 4 == 0) & (anho % 100!= 0) | (anho % 400==0)
    return restultadp

print("\n---------------------------")
print(isBisiesto(anho))

print("\n-----años bisiestos----------------------")
for i in range(1600, 2100+1):
    if isBisiesto(i):
        print(i, end=' ')


print("\n\n-----aquí la función----------------------")
anho = int(input("Ingrese el año(numero entero): "))

def bisiesto(anho):
    if isBisiesto(anho):
        restult = "el año "+ str(anho)+ " es bisiesto"
    else:
        restult = "el año "+ str(anho)+ " no es bisiesto"
    return restult 

print(bisiesto(anho))
