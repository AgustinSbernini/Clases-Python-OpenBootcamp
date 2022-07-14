#TODO Programacion multihilo 

import _thread
import time
import logging

def horaActual(nombreThread, delay):
    count = 0
    #TODO logging sirve para mandar mensajes por consola y tienen un orden de severidad. Para modificar desde cual queres mostrar
    # Hay que usar basicConfig y el nombre del nivel va en mayus
    logging.basicConfig(level=logging.DEBUG)
    while count < 0:
        time.sleep(delay)
        count += 1
        print(f'El hilo {nombreThread} marca que son las: {time.ctime(time.time())}')
        match count:
            case 1:
                logging.debug("Camino erroneo\n")
            case 2:
                logging.info("No entres ahí\n")
            case 3:
                logging.warning("Advertencia, camino equivocado\n")
            case 4:
                logging.error("Ultimo aviso, va a pasarla mal\n")
            case 5:
                logging.critical("Usted esta morido\n")


_thread.start_new_thread(horaActual,("Juan", 1))
_thread.start_new_thread(horaActual,("Fernando", 2))

print("Han pasado los threads")
#TODO Dormir programa para que le de tiempo suficiente para que se ejecuten los hilos
time.sleep(4)
    

#TODO filter se le pasan dos parametros, el primer la condicion, el segundo la lista. Va a recorrer y guardar los resultados
# donde la condicion sea == True. Retorna la lista resultante. Es tipo filter, por lo cual hay que parsearlo.

numeros = [1,2,3,4,5,6,7,8,9,10]

def buscarPares(x):
    retorno = False
    if x % 2 == 0:
        retorno = True
    return retorno

resultado = filter(buscarPares,numeros)
#resultado = filter(lambda x : x % 2 == 0, numeros) Otra opcion usando lambda (funcion anonima)
print(type(resultado))
print(list(resultado))

#TODO map aplica una funcion a todos los elementos de un objeto iterable (lista o tupla)
# Retorna la lista resultante. Es tipo map, por lo cual hay que parsearlo.

def aumento (x):
    return round(x*1.1,2)

resultado = map(aumento, numeros)
print(type(resultado))
print(list(resultado))

#TODO reduce ejecuta una funcion sobre la lista hasta que la lista se quede con un unico elemento.

from functools import reduce

def suma(a, b):
    print(f'a = {a} y b = {b}')
    return a + b

resultado = reduce(suma, numeros)
print(type(resultado))
print(resultado)


#TODO zip combina multiple cosas en una lista uniendo elemento a elemento

cursos = ["Java","Python","Git"]
precio = [80,130,40]
profesor = ["Juan","Fer","Pedro"]

resultado = zip(cursos, precio, profesor)

print(type(resultado))
print(list(resultado))


#TODO all y any sirve para verificar si se cumple todas o al menos una condicion de una lista.

lista = [1 == 1, 2 == 2, 3 == 4]

resultado = all(lista)
print(type(resultado))
print(resultado)

resultado = any(lista)
print(type(resultado))
print(resultado)


#TODO min y max devuelve el menor valor o el maximo valor de una lista

print(f'El minimo es {min(numeros)}')
print(f' El maximo es {max(numeros)}')