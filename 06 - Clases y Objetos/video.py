# POO Programacion orientada a objetos
# Un Objeto es una representacion en lenguaje de programacion de algo de la vida real
#TODO Los objetos poseen metodos que son acciones que realizamos
#TODO Una propiedad es algo que le pertenece a ese objeto y puede mutar
# Los objetos se crean inicializandolo con una clase
#TODO Si una propiedad o un metodo empieza con un _ no deberíamos modificarlo fuera de la class

class Estatica: #TODO Clase estatica no se deben instanciar, utilizan un solo espacio de memoria que va modificandose
    numero = 1
    def incrementa():
        Estatica.numero+=1

Estatica.incrementa()
print(Estatica.numero,"\n")
Estatica.incrementa()
print(Estatica.numero,"\n")
Estatica.incrementa()
print(Estatica.numero,"\n")


class Juguete: #TODO Clase dinamica se deben instanciar y reserva un espacio de memoria para cada instancia
    _estadoLuz = False #Propiedad

    def cambiaLuz(self): #Metodo
        self._estadoLuz = True ^ self._estadoLuz # self == this

    def isEstadoLuz(self):
        if(self._estadoLuz == True):
            return "La luz esta encendida\n"
        else:
            return "La luz esta apagada\n"

class Dino(Juguete): #TODO Is-a Herencia Dino ES un juguete
    _despierto = False

    def cambiarDespierto(self):
        self._despierto = True ^ self._despierto

    def isDespierto(self):
        if(self._despierto == True):
            return "El dino esta despierto\n"
        else:
            return "El dino esta dormido\n"

class Ave:
    alas = False

class Terodactilo(Dino, Ave): #TODO Herencia multiple y Herencia nivel
    _alimentado = False

    def cambiarAlimento(self):
        self._alimentado = True ^ self._alimentado

    def isAlimentado(self):
        if(self._alimentado == True):
            return "El terodactilo esta alimentado\n"
        else:
            return "El terodactilo no esta alimentado\n"   


miTero = Terodactilo() #inicializar / Instanciar
miTero.cambiaLuz()
print(miTero.isEstadoLuz())
miTero.cambiaLuz()
print(miTero.isEstadoLuz())
miTero.cambiaLuz()
print(miTero.isEstadoLuz())
miTero.alas = True
miTero.cambiarDespierto()
miTero.cambiarAlimento()
print(miTero.isAlimentado(),miTero.isDespierto(), sep="")
print(dir(miTero), "\n") #TODO dir(class) te muestra todas las funciones que tiene esa clase. Incluye las heredadas


class padrePrueba:
    def __init__(self):
        print("Init padre")

class pruebasFuncionesDefinidas(padrePrueba):
    nombre = None
    color = None

    def __init__(self, nombre, color): #TODO Inicializador se les agrega los parametros, si es necesario, para crear el objeto
        super().__init__() #TODO Inicializa la clase padre.
        print("Init prueba\n")
        self.nombre = nombre
        self.color = color

    def __del__(self): #TODO destructor se ejecuta automaticamente cuando ya no se encuentra referencia a la clase
        print("\nDesctructor de prueba\n") # Se invoca como del(class) si se quiere usar antes


prueba = pruebasFuncionesDefinidas("Jorge", "Azul")
print(prueba.nombre, prueba.color,"\n")

#TODO Class abstract se debe realizar un import de ABC y realizar una anotacion
from abc import ABC, abstractmethod

class Animal(ABC): #La clase abstract debe heredar de ABC
    @abstractmethod #Anotacion que obliga a las clases hijas a usar la funcion
    def sonido(self):
        pass
    def diHola(self): #Por lo tanto esta no es necesario que la declaren. Pueden utilizarla igual.
        print("Saludando")

#a = Animal() Las clases abstract no se pueden instanciar. Solo se pueden derivar (usar como clase padre)
class Perro (Animal):
    #pass no se podría hacer un pass porque se necesita utilizar los metodos de la clase abstract si o si
    def sonido(self):
        print("Wow")

class Gato (Animal):
    def sonido(self):
        print("Miau")

perrito = Perro()
perrito.sonido()
perrito.diHola()
gatito = Gato()
gatito.sonido()
print("")

#TODO Has-a Composicion Es un tipo de relacion donde contiene a la otra clase. Es la competencia de la herencia

class Motor:
    tipo = "Diesel"

class Ventana:
    cantidad = 6
    def cambiarCantidad(self, valor):
        self.cantidad = valor
class Ruedas:
    cantidad = 4

class Carroceria:
    ventana = Ventana()
    ruedas = Ruedas()

class Coche: #Coche CONTIENE un motor y una carroceria
    carroceria = Carroceria()
    motor = Motor()

suran = Coche()
print("La cantidad de ventanas del auto es:",suran.carroceria.ventana.cantidad)
suran.carroceria.ventana.cambiarCantidad(9) # Es mas claro que la herencia para poder ver el orden de jerarquias
print("La cantidad de ventanas del auto despues del cambio es:",suran.carroceria.ventana.cantidad)

print(suran) #Arroja tipo de objeto y direccion de memoria