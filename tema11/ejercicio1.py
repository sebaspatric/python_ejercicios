'''
crear una tabla llamada Alumnos que constará de tres columnas: la columna id tipo entero, la columna nombre tipo texto, la columna apellido tipo texto.
una vez creado la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
por último realizar una búsqueda de un alumno por nombre y mostrar los datos por consola
'''
import sqlite3

def main():
    num = int(input("Ingrese el número de alumnos que desea crear: "))
    insersiones(num)
    nombre = input("Ingrese nombre a buscar: ")
    buscar_alumno(nombre)


def insersiones(num):
    for i in range(num):
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        crear_tabla(nombre, apellido)
        



#creación de la tabla
def crear_tabla(nombre, apellido):
    #conexión a la base de datos
    conn = sqlite3.connect('alumnos.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT)''')
    
    query = '''INSERT INTO alumnos (nombre, apellido) VALUES (?,?)'''

    rows = c.execute(query,(nombre, apellido))
    conn.commit()
    c.close()
    conn.close()

#busqueda alumno
def buscar_alumno(nombre):
    #conexión a la base de datos
    conn = sqlite3.connect('alumnos.db')
    c = conn.cursor()
    query = "SELECT * FROM alumnos WHERE nombre =?"

    rows = c.execute(query,(nombre,))
    alumno = rows.fetchone()

    if alumno is not None:
        print(f'Id: {alumno[0]}')
        print(f"Nombre: {alumno[1]}")
        print(f"Apellido: {alumno[2]}")
    else:
        print("No existe el alumno")
    c.close()
    conn.close()




if __name__ == '__main__':
    main()