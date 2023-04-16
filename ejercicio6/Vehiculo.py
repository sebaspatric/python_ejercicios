class Vehiculo:
    color = None
    ruedas = None
    puertas = None
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
class Coche(Vehiculo):
    velocidad = None
    cilindrada = None
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

#c = Coche('blanco', 10, 10, 100)
c = Coche('blanco', 4, 5, 100, 300)
print(c)
print("color =",c.color, "\nruedas = ", c.ruedas, "\npuertas = ", 
      c.puertas, "\nvelocidad = ", c.velocidad, "\ncilindrada = ", c.cilindrada)