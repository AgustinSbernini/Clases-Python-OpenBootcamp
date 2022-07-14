#TODO tkinter genera tcl (otro lenguaje) y lo ejecuta por debajo
import tkinter
#TODO ttk toolkit para que tenga estilo del sistema operativo
from tkinter import ttk

#TODO widget (componente o controles u objetos) botones, etiquetas, caja de texto, etc. 

window = tkinter.Tk()
print(type(window))

#TODO label donde se le pasa la ventana en la cual se va a generar y se le adjunta un texto
# bg = background = fondo de la letra. fg = foreground = color de la letra.
# ipad x(ancho) o y(alto) = inner padding = espacio entre un borde y el texto. Cuenta desde donde empieza el widget hasta el borde
# padx o pady en lugar de empujar desde el texto deja un margen.
# fill = relleno = puede ser 'x', 'y' (sin expand no funciona bien) o 'both'. expand = queda centrado cuando expandis la ventana
# side = para alinear a algun extremo, puede ser 'left', 'right', 'top', 'bottom'

#TODO geometria pack

#label_saludo = tkinter.Label(window, text = "Holaaa!", bg = "yellow", fg = "blue")
#label_saludo.pack(ipadx = 50, ipady = 50, fill = 'both', expand = True)

#label_adios = tkinter.Label(window, text = "Adioos!", bg = "black", fg = "white")
#label_adios.pack(ipadx = 50, ipady = 50, fill = 'both', expand = True)

#TODO Geometria mediante grid funciona como una hoja de excel

# Con columconfigure informas cuantas filas y columnas va a tener el grid
# Se le indica fila y columna donde va a ir ubicado el label.
# Sticky sirve para fijar el texto en una posicion de la ventana. Usa la rosa de los vientos.
# Entry sirve para poner una entrada de texto 
# Dentro del Entry podemos usar show = ' ' para que se muestre lo que querramos mientras escribimos 

# window.columnconfigure(0, weight = 1)
# window.columnconfigure(0, weight = 3)

# usarname_label = ttk.Label(window, text = "Username:")
# usarname_label.grid(row = 0, column = 0, sticky = tkinter.W, padx = 5, pady = 5)

# username_entry = ttk.Entry(window)
# username_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

# password_label = ttk.Label(window, text = "Password:")
# password_label.grid(row = 1, column = 0, sticky = tkinter.W, padx = 5, pady = 5)

# password_entry = ttk.Entry(window, show = '*')
# password_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

# logging_button = ttk.Button(window, text = "Login")
# logging_button.grid(row = 2, column = 2, sticky = tkinter.W, padx = 5, pady = 5)


#TODO Geometria place sirve para posicionar de forma absoluta dentro de una ventana o relativa a un elemento

# label1 = tkinter.Label(window, text = "primer label", bg = 'black', fg = 'white')
# label1.place(x = 10, y = 15)

# label2 = tkinter.Label(window, text = "segundo label", bg = 'black', fg = 'white')
# label2.place(x = 150, y = 15)


#TODO Frame es un marco donde se pueden ubicar elementos adentro, se usa principalmente para agrupar elementos.

# frame = tkinter.Frame(window)
# frame.grid(column=0,row=0)
# frame2 = tkinter.Frame(window)
# frame2.grid(column=1,row=1)

# label = tkinter.Label(frame, text = "label dentro de frame")
# label.grid(column=0,row=0)
# label1 = tkinter.Label(frame, text = "label dentro de frame 1 . 1")
# label1.grid(column=1,row=1)

# label2 = tkinter.Label(frame2, text = "label dentro de frame")
# label2.grid(column=0,row=0)
# label3 = tkinter.Label(frame2, text = "label dentro de frame 1 . 1")
# label3.grid(column=1,row=1)


#TODO Listbox es una lista donde podes seleccionar las opciones descriptas
# Hay que crear una lista y luego transformarla en una variable que pueda reconocer tkinter

# lista = ['Argentina', 'Brasil', 'Uruguay', 'Francia', 'España', 'Italia']
# listaItems = tkinter.StringVar(value = lista)
# print(type(listaItems))

# listbox = tkinter.Listbox(window, height = 20, width= 15, listvariable= listaItems)
# listbox.grid(column=0,row=0)


#TODO Radiobutton son botones redondos con un texto al lado que se usan para seleccionar opciones
# Se le asigna un value = 'x' que es el valor que devuelven al seleccionarse.
# Los botones se agrupan a traves de la opcion variable = 'VariableDondeSeGuardaElValor'. Solo se podra elegir entre 1 de estos

# valorGuardado = tkinter.StringVar()
# valorGuardado2 = tkinter.StringVar()

# button1 = ttk.Radiobutton(window, text = "Opcion A", value = 1, variable = valorGuardado)
# button2 = ttk.Radiobutton(window, text = "Opcion B", value = 2, variable = valorGuardado)
# button3 = ttk.Radiobutton(window, text = "Opcion C", value = 3, variable = valorGuardado)

# button1.grid(row = 0, column = 0)
# button2.grid(row = 1, column = 0)
# button3.grid(row = 2, column = 0)

# button4 = ttk.Radiobutton(window, text = "Opcion A", value = 1, variable = valorGuardado2)
# button5 = ttk.Radiobutton(window, text = "Opcion B", value = 2, variable = valorGuardado2)
# button6 = ttk.Radiobutton(window, text = "Opcion C", value = 3, variable = valorGuardado2)

# button4.grid(row = 0, column = 1)
# button5.grid(row = 1, column = 1)
# button6.grid(row = 2, column = 1)


#TODO Checkbutton boton cuadrado que se tilda al clickearlo

# valorGuardado = tkinter.StringVar()

# checkbox = tkinter.Checkbutton(window, text = "Acepto terminos y condiciones",variable = valorGuardado)
# checkbox.grid(row = 0, column = 0)


#TODO Evento cuando se realiza alguna accion dentro de la ventana. Estos requieren un call back para funcionar (una funcion)
# Esto se realiza a traves de un binding donde se le pasa que es lo que va a realizar la accion y el call back que produce.

def saludar(event):
    print ("Hola, que tal?")

def saludar2(event):
    print("Hola, como te va?")

def saludar3(event):
    print("Hola, que haces?")

def salir(event):
    print("Esta es la despedida")
    window.quit()

boton = tkinter.Button(window, text = "Haz click")
boton.pack()
boton.bind('<Button-1>', saludar) #Click derecho
boton.bind('<Button-2>', saludar2) #Click central (ruedita)
boton.bind('<Button-3>', saludar3) #Click izquierdo

boton = tkinter.Button(window, text = "Salir")
boton.pack()
boton.bind('<Button-1>', salir)


#TODO loop para mantener abierto y en ejecución el programa
window.mainloop()