class Alumno:
    #atributos
    nombre = ""
    nota = 0
    #metodo constructor
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    #metodo string
    def __str__(self):
        return "nombre: {0}, nota: {1}".format(self.nombre, self.nota)
    #metodo nota
    def aprobado(self):
        if self.nota >= 4:
            return True
        else:
            return False    
    def mensaje(self):
        if self.aprobado():
            return "Nota {} Aprobado".format(self.nota)
        else:
            return "Nota {} Rechazado".format(self.nota)

a1 = Alumno("Juan", 5)
a2 = Alumno("Pedro", 4)
a3 = Alumno("Maria", 3)

print(a1)
print(a1.mensaje())
print("-------------------")
print(a2)
print(a2.mensaje())
print("-------------------")
print(a3)
print(a3.mensaje())