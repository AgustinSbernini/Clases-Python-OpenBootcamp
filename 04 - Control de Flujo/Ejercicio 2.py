#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numeroInicial = 3
numeroFinal = 14
for numeroImpar in range(numeroInicial,numeroFinal):
    if (numeroImpar % 2 == 1):
        print("El numero", numeroImpar, "es impar")
