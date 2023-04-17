import pickle


class Vehicculo:
    marca = ''
    modelo = ''
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def __str__(self):
        return f'marca = {self.marca}, \nmodelo = {self.modelo}'

#serializacion
v1 = Vehicculo('Ford', 'Mustang')
archivo = "vehiculo.dat"
f = open(archivo, 'wb')
pickle.dump(v1, f)
f.close()

#deserializacion
f2 = open(archivo, 'rb')
v2 = pickle.load(f2)
f2.close()

print(v2)

