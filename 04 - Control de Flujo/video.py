#TODO Control de flujo de un programa es guiar la ejecución en torno a una cantidad de condiciones que se cumplan o no.
# Se guían a través de un test de veracidad
#TODO Operadores de comparacion >, <, >=, <=, ==, !=
#TODO Operadores conectores & (and) | (or) ^ (xor(uno u otro))
#TODO in / not in para verificar si estan dentro o no estan dentro

a = 5
b = 10
lista = ['a',2,7,"Hola Mundo"]
listaNumerica = [2,5,1,7]
i = 0

resultado = ((a < b) ^ (a != 5))
print("\n\n",resultado,"\n")

#TODO if no hay {} se ejecuta todo lo que este identado
if(a > b):
    print("hola")
    print("jorge\n")
elif (a < b): #Se usa elif en vez de elseif
    print("perrun\n") 
else:
    if(a == 5):
        print("mamasitaaaa") #Esto esta dentro del segundo if
    print("ppa\n") #Esto esta dentro del else

if "pepe" not in lista:
    print("pepe no esta en la lista\n")

#TODO While por identacion. continue fuerza la siguiente iteración del while evitando que se ejecute el resto del codigo.
# break termina el while
while (a < b):
    print("a vale ", a)
    a+=1
    if(a % 2 == 0):
        continue
    print("a vale ", a)
print("\n")


#TODO for tomaValor in aRecorrer. Recorre lo que sea que le pasemos, tuplas, listas, rangos.
# range(x) del 0 a x, (5,10) del 5 al 9
for j in range(5,10):
    print("j vale", j)
    if(j == 2):
        break
else: #TODO for else se ejecuta cuando dentro del for no se ejecuto el break
    print("No se encontró el j == 8")

print("\n")
for valor in lista:
    print("Dentro de la lista en la posición",i,"se encuentra",valor)
    i+=1

#TODO sorted te ordena una lista numerica O de letras, pero no combinación. Agregando reverse = True hace descendente
print("\n",listaNumerica)
listaNumerica = sorted(listaNumerica, reverse = True)
print(listaNumerica)

#TODO switch match Aca no existe switch, se usa match. No tiene breaks ni default.
match listaNumerica[0]:
    case 1:
        print("es 1")
    case 2:
        print("es 2")
    case 5:
        print("es 5")
    case 7:
        print("es 7")

#TODO pass se utiliza para dejar condicionales o bucles vacios
if a < 2:
    pass
