'''
crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un boton de reinicio para que deje todo como al principio

Al principio no tiene qque haber una opción seleccionada
'''

import tkinter as tk
from tkinter import DISABLED
from tkinter import ttk
from tkinter.ttk import Button

def crear_lista_de_opciones():
    lista_de_opciones = []
    selected = tk.StringVar()
    selected.set(None)
    list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
    j = 0
    for i in list:
        a = tk.Radiobutton(text=i, variable=selected, value=i)
        #agrega balor a lista de opciones según listado
        lista_de_opciones.append(a)
        #crea grilla
        a.grid(row=j, column=0)
        j += 1
    boton_reinicio = crear_boton_reinicio(j)
    lista_de_opciones.append(boton_reinicio)
    return lista_de_opciones


def crear_boton_reinicio(fila):
    boton_reinicio = Button(text="Reiniciar", command=reiniciar)
    boton_reinicio.grid(row=fila, column=0)
    return boton_reinicio


def reiniciar():
    global lista_de_opciones
    lista_de_opciones = crear_lista_de_opciones()
    global boton_reinicio
    #boton_reinicio = crear_boton_reinicio()
    #boton_reinicio.grid(row=0, column=0)
    #boton_reinicio.config(state=DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ejemplo de RadioButton")
    #root.geometry("300x300")
    #root.resizable(False, False)

    lista_de_opciones = crear_lista_de_opciones()
    #boton_reinicio = crear_boton_reinicio()
    #boton_reinicio.grid(row=0, column=0)
    #boton_reinicio.config(state=DISABLED)
    
    root.mainloop()