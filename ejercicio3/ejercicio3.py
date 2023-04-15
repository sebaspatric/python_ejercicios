#>>>> ###>>>>> >>>>>
peso = input("indique su peso en (kg): ")
#>ndique su peso en (kg): 70
estatura = input("indique su estatura en metros[m]: ")
# dique su estatura en metros[m]: 1.7
type(estatura)
#<  nclass 'str'>
type(peso)
##class 'str'>
imc = round(float(peso)/float(estatura)**2,2)
type(imc)
#<class 'float'>
print(imc)
#24.22
print("Tu índice de masa corporal es: "+str(imc))

#Tu índice de masa corporal es: 24.22



