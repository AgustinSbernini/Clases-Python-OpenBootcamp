# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

from re import S


class Vehiculo:
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = None
    cilidrada = None

    def __init__(self, velocidad, cilidrada, color, ruedas, puertas):
        Vehiculo.__init__(self, color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilidrada = cilidrada


suran = Coche(120, 16, "Gris", 4, 5)

print("\nEl auto suran tiene las siguientes propiedades:")
print("    Su velocidad maxima es:",suran.velocidad)
print("    Su cantidad de puertas es:",suran.puertas)
print("    Su cilidrada es:",suran.cilidrada)
print("    Su cantidad de ruedas es:",suran.puertas)
print("    Su color es:",suran.color)