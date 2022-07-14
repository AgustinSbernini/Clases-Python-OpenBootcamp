# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora:
# sumar, restar, multiplicar y dividir.
# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. 
# Los resultados tenéis que mostrarlos por consola.

import operaciones.operaciones as op

operador = op.Operador()
numero1 = float(input("Ingrese un primer numero: "))
numero2 = float(input("Ingrese un segundo numero: "))

print("El resultado de la suma es:",op.suma(numero1, numero2))
print("El resultado de la resta es:",op.resta(numero1, numero2))
print("El resultado de la multiplicacion es:",operador.multiplicador(numero1, numero2))
print("El resultado de la divisiones es:",op.dividir(numero1, numero2))
