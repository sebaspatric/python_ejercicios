'''
crea un script que pida al usuario una lista de países (separados por comas).
Éstos se deben almacenar en una lista. No debería haber países repetidos 
(haz uso de set). Finalmente, muestra por consola la lista de paísees ordenados 
alfabéticamente y separados por comas.

'''

import sys

def main():
    pais = []
    print('Lista de países: ingrese un país o escriba done para terminar')
    while True:
        pais.append(input('Ingrese un país: '))
        if pais[-1] == 'done':
            break
    pais.remove('done') 
    paisset = set(pais)
    paislist = list(paisset)
    print(f'lista de paises entregada: {pais}')
    print(f'lista de países obtenida: {paislist}')
    print(f'lista de paises ordenados alfabéticamente: {sorted(pais)}')
    print(f'no repetidos: {paisset.intersection(pais)}')
    print(f'no repetidos ordenados: {sorted(paisset)}')
 

if __name__ == '__main__':
    main()
    