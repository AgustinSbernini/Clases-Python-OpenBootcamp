#TODO mostrar en pantalla distintas maneras

numero, texto, otroNum = 51, "El perro", 2.5

#Forma vieja, viene de C
print("\nEl primer numero es %d, el texto dice %s, y el ultimo numero es %.2f \n" %(numero, texto, otroNum)) 

#Forma vieja, se uso hasta la 3.6
print("\nEl primer numero es {}, el texto dice {}, y el ultimo numero es {} \n".format(numero, texto, otroNum))
print("\nEl primer numero es {2}, el texto dice {0}, y el ultimo numero es {1} \n".format(texto, otroNum, numero))
print("\nEl primer numero es {n1}, el texto dice {t1}, y el ultimo numero es {f1} \n".format(n1=numero, t1=texto, f1=otroNum))

#TODO print(f'texto') Mejor manera. Se puede usar codigo Python dentro de las llaves. Es la mas flexible y claro.
print(f"\nEl primer numero es {numero}, el texto dice {texto.upper()}, y el ultimo numero es {otroNum} \n")


#TODO diff str y repr es que str se utiliza de manera formal para mostrar al usuario y repr de forma tecnica para desarrollo o depuracion
class Juguete:
    nombre = None
    precio = None

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self) -> str:
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'


dino = Juguete("Dino", 10)
dinoStr = str(dino)
print(dino, "\n") #Representacion informal editado con __str__, codigo de produccion // Lo mismo que hacer print(str(dino))
print(dinoStr, "\n") #Otra manera
print(repr(dino), "\n") #Representacion tecnica, codigo depuracion o desarrollo.


#TODO ficheros open abre con modos: 'r'(read) 'w'(write) 'a'(append) 'x'(create (no sirve))  se le agrega 't'(texto) o 'b'(bin)

#TODO lectura de ficheros
f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs\\data.csv", 'r')
ficheroEntero = f.read() #Lee todo el fichero dentro del () se podría poner la cantidad de bytes que se quieren leer.
f.close()
f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs\\data.csv", 'r')
lineas = f.readline() #Lee de a una sola linea, se puede ejecutar varias veces (for o while) y se va sobreescribiendo
f.close()
f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs\\data.csv", 'r')
lineasEnLista = f.readlines() #Lee todo el fichero y guarda cada linea en un elemento de la lista (incluye los \n)
f.close()

print("ficheroEntero:\n",ficheroEntero)
print("lineas:\n",lineas)
print("lineasEnLista:\n",lineasEnLista,"\n")

#TODO Escritura de ficheros

f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs\\primerWrite.txt", 'w')
f.write("dato1\n") #Escribe el texto literal escrito, necesario poner el \n para el salto de linea
f.write("dato2\n")
f.close()

f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs\\SegundoWrite.txt", 'w')
lista = ["dato1","dato2","dato3"]
f.writelines(lista) #Escribe una lista, necesario poner el \n para el salto de linea
f.close()

#Manera de automatizarlo
f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs\\tercerWrite.txt", 'w')

for linea in lista:
    if not linea.endswith("\n"):
        linea += "\n"
        f.write(linea)

f.close()

#TODO pickle es un modulo que te permite serializar (parsear) y deserealizar datos en un fichero
import pickle #Recordar usar en binario

dogi = Juguete("Perrin", 7.5)
f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs\\juguetitos.bin","wb")
pickle.dump(dogi,f) #Se parsea poniendo pickle.dump(objeto, fichero)
f.close()

f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs\\juguetitos.bin", 'rb')
perrin = pickle.load(f) #Se desparsea poniendo objeto = pickle.load(fichero)
f.close()

print(f"{perrin.nombre} tiene un valor de {perrin.precio}\n")