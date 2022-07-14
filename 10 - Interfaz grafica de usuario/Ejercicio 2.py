# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, 
# también debe de tener un label con el texto que queráis.
import tkinter

window = tkinter.Tk()

label = tkinter.Label(text = "Cual es la moneda oficial de Argentina?")
label.grid(columnspan = 3, row = 0)

listaDeMonedas = ['Dolar', 'Pesos', 'Euros', 'Libra']
listaDeMonedasItem = tkinter.StringVar(value = listaDeMonedas)

listbox = tkinter.Listbox(window, height = 4, width = 10, listvariable = listaDeMonedasItem)
listbox.grid(column = 1, row = 1)

tkinter.mainloop()