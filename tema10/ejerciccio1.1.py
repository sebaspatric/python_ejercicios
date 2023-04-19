'''
crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un boton de reinicio para que deje todo como al principio

Al principio no tiene qque haber una opción seleccionada
'''
from tkinter import ttk
import tkinter as tk


class RadiobuttonList:
    def __init__(self, parent, options):
        self.var = tk.StringVar()
        self.var.set(None)
        self.options = options
        self.buttons = []

        #crear los botones de radio
        for option in self.options: # de la lista...
                                                #asigna nombre y valor de la opción
            button = tk.Radiobutton(parent, text=option, variable=self.var, value=option)
            self.buttons.append(button)
            button.pack()
        
        #crear el boton de reinicio
        self.reset_button = tk.Button(parent, text="Reiniciar", command=self.reset)
        self.reset_button.pack()
    
    def reset(self):
        self.var.set(None)
        #for button in self.buttons:
        #    button.deselect()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Radiobutton List")
    root.geometry("300x200")

    #crear una lista de RadioButton
    options = ["A", "B", "C"]
    radio_list = RadiobuttonList(root, options)
#------------------------------------------------------------

#--------------------------------------------------------------------
    root.mainloop()

