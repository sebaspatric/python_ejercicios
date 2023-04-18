'''
crear una aplicacion que obtendrá los elementos impares de una lista pasada por parámetro con filter
y realizará una suma de  todos estos elemenos obtenidos mediante reduce
'''


from functools import reduce


def main():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 5]
    lista2 = [1, 2, 3, 4, 5]
    e = impares(lista1)
    print(e)

    listaImpares = list(filter(lambda x: x % 2!= 0, lista2))
    print(listaImpares)

    suma1 = reduce(lambda x, y: x + y, listaImpares)
    print(suma1)

    suma2 = sumaImpares(lista2)
    print(suma2)

def impares(lista):
    return [x for x in lista if x % 2!= 0]

def sumaImpares(lista):
    lista = list(filter(lambda x: x % 2!= 0, lista))
    return reduce(lambda x, y: x + y, lista)

if __name__ == '__main__':
    main()  