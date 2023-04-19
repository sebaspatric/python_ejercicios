import sys
import tkinter as tk
from tkinter import ttk

window = tk.Tk() #generar ventana

#grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tk.StringVar() #variable value

r1 = ttk.Radiobutton(window, text="Radio 1", variable=selected, value = '1')
r2 = ttk.Radiobutton(window, text="Radio 2", variable=selected, value = '2')
r3 = ttk.Radiobutton(window, text="Radio 3", variable=selected, value = '3')

#posiciones
r1.grid(row=0, column=0)
r2.grid(row=1, column=0)
r3.grid(row=2, column=0)

#---------------------------------

selected2 = tk.StringVar() #variable value
rs1 = ttk.Radiobutton(window, text="Radio 1", variable=selected2, value='12')
rs1.grid(row=0, column=1)

window.mainloop() #loop

sys.exit(0)

