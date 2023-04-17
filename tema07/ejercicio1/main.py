from modulo1 import sumar as s, restar as r, multiplicar as m, dividir as d

def main():
    x = 10
    y = 20
    #print(type(x))
    #print(type(y))
    
    sum = s(x,y)
    rest = r(x, y)
    mult = m(x, y)  
    div = d(x, y)  
    texto = "valores x = {}, y = {}".format(x, y)
    print(texto)
    print("suma =", sum)
    print("resta =", rest)
    print("multiplicacion =", mult)
    print("division =", div)










if __name__ == '__main__':
    main()
