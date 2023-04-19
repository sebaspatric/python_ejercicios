'''
crear una interfaz sencilla la cual debe contener una lista de elementos seleccionables y un label

'''
import tkinter as tk

#creamos la ventana principal
root = tk.Tk()

#creamos un label con texto
label = tk.Label(root, text="elemento de lista")

#lista de elementos
elementos = ["Argentina", "Brasil", "Colombia", "Ecuador", "Peru"]
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.insert(1, "Brasil")
listbox.insert(2, "Colombia")
listbox.insert(3, "Ecuador")
listbox.insert(4, "Peru")


#posicionar elementos
label.pack()
listbox.pack()

# bucle
root.mainloop()
