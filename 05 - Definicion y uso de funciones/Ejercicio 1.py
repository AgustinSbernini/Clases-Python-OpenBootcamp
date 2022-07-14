# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros 
# y otra función que calcule el área de un círculo recibiendo el radio del mismo.
import math

def calcularAreaTriangulo(base, altura):
    base = float(base)
    altura = float(altura)
    area = (base * altura) /2
    return area

def calcularAreaCirculo(radio):
    radio = float(radio)
    area = math.pi * (radio**2)
    return area


base = input("Ingrese la base del triangulo: ")
altura = input("Ingrese la altura del triangulo: ")
areaTriangulo = calcularAreaTriangulo(base, altura)
print("El area del triangulo es:",areaTriangulo)

radio = input("Ingrese el radio del circulo: ")
areaCirculo = calcularAreaCirculo(radio)
print("El area circulo es:",round(areaCirculo,2))