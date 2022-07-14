#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

lista = []
for numero in range(101):
    lista.append(numero)

lista = sorted(lista, reverse = True)

for numero in lista: 
    if(numero == 0):
        print(numero)
        break
    print(numero, end = ", ")