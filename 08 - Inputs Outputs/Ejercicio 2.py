# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, 
# lo guardaréis en un archivo y luego lo cargamos.
import pickle

class Vehiculo:
    tipo = None
    ruedas = None
    puertas = None
    color = None

    def __init__(self, tipo, ruedas, puertas, color):
        self.tipo = tipo
        self.ruedas = ruedas
        self.puertas = puertas
        self.color = color

miAuto = Vehiculo("Suran",4,5,"Gris")

f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs.py\\archivo.bin",'wb')
pickle.dump(miAuto, f)
f.close()

f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs.py\\archivo.bin",'rb')
miAutoCargado = pickle.load(f)
f.close()

print(f'Mi auto es una {miAutoCargado.tipo}, tiene {miAutoCargado.ruedas} ruedas, tiene {miAutoCargado.puertas} puertas y es de color {miAutoCargado.color}')
