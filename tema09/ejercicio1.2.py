'''
crea un script que pida al usuario una lista de países (separados por comas).
Éstos se deben almacenar en una lista. No debería haber países repetidos 
(haz uso de set). Finalmente, muestra por consola la lista de paísees ordenados 
alfabéticamente y separados por comas.

'''

import sys

def main():
    paises = []
    lista = input('lista de países (separados por comas): ')
    for pais in lista.split(','):
        paises.append(pais.strip())
    paisesNorepetidos = list(set(paises))
    paisesOrdenados = sorted(paisesNorepetidos)
    print(paises)
    print(paisesNorepetidos)
    print(paisesOrdenados)



 

if __name__ == '__main__':
    main()
    