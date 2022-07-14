# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre 
# y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado 
# de la nota y si ha aprobado o no.

class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

alumno1 = Alumno("Juan Gomez","9")
alumno2 = Alumno("Gabriel Perez","3")

print("El alumno", alumno1.nombre,"tuvo como nota un",alumno1.nota,end = ", ")
if(int(alumno1.nota) > 6):
    print("por lo tanto se encuentra aprobado")
else:
    print("por lo tanto se encuentra desaprobado")

print("El alumno", alumno2.nombre,"tuvo como nota un",alumno2.nota,end = ", ")
if(int(alumno2.nota) > 6):
    print("por lo tanto se encuentra aprobado")
else:
    print("por lo tanto se encuentra desaprobado")