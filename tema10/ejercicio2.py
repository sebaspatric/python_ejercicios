'''
crear una interfaz sencilla la cual debe contener una lista de elementos seleccionables y un label

'''
import tkinter as tk

#creamos la ventana principal
ventana = tk.Tk()
#agregar titulo
ventana.title("Prueba")
#creamos un label con texto
label = tk.Label(ventana, text="Prueba")

#lista de elementos
elementos = ["Argentina", "Brasil", "Colombia", "Ecuador", "Peru"]

#objeto que almacena el elemento
elemento = tk.StringVar()

#funcion que se ejecuta cuando se selecciona un elemento
def mostrar_elemento():
    seleccionado = elemento.get()
    print(f"Se selecciono {seleccionado}")

#lista desplegable con los elementos
lista = tk.OptionMenu(ventana, elemento, *elementos)


#crear boton
boton = tk.Button(ventana, text="Mostrar", command=mostrar_elemento)

#mostramos
label.pack()
lista.pack() 
boton.pack()

#loop
ventana.mainloop()