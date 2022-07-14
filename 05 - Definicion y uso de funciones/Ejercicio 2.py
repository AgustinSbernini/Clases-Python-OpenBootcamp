# Escribe una función que pueda decirte si un número (número entero) es primo o no.
def calcularSiEsPrimo (numero):
    resultado = True
    numero = int(numero)
    for i in range(2, numero):
        if(numero % i == 0):
            resultado = False
            break

    return resultado
print("\n")
for i in range(1,40):
    numeroResultante = calcularSiEsPrimo(i)
    if(numeroResultante):
        print(i, "es numero primo\n")
    else:
        print(i, "No es numero primo\n")