# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. 
# No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados 
# alfabéticamente y separados por comas.

listaDePaises = []

while True: 
    pais = input("Ingrese un pais(Ingrese un numero para finalizar): ")
    if(pais.isnumeric()):
        break
    else:
        listaDePaises.append(pais)

conjuntoDePaises = sorted(set(listaDePaises))
print(conjuntoDePaises)