# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por 
# parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce

listaNumerica = [1,2,3,4,5,6,7,8,9,10]

def numerosImpares(num):
    retorno = False
    if num % 2 == 1:
        retorno = True
    return retorno

def sumaNumeros(num1, num2):
    return (num1 + num2)

print(reduce(sumaNumeros,(list(filter(numerosImpares, listaNumerica)))))


