# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y 
# que contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.
import tkinter
from tkinter import ttk 

window = tkinter.Tk()

def resetValues(event):
    savedValue.set(None)

savedValue = tkinter.StringVar()

label = tkinter.Label(window, text = "Cual pais tiene una mayor poblacion?")
label.grid(column = 0, row = 0)

button1 = ttk.Radiobutton(window, text = "Argentine", value = '1', variable = savedValue)
button2 = ttk.Radiobutton(window, text = "Brazil", value = '2', variable = savedValue)
button3 = ttk.Radiobutton(window, text = "Chinese", value = '3', variable = savedValue)

button1.grid(column = 1, row = 1, sticky = tkinter.W)
button2.grid(column = 1, row = 2, sticky = tkinter.W)
button3.grid(column = 1, row = 3, sticky = tkinter.W)

buttonReset = tkinter.Button(window, text = "Reset")
buttonReset.grid(column = 2, row = 4, sticky = tkinter.SE)
buttonReset.bind('<Button-1>', resetValues)

tkinter.mainloop()