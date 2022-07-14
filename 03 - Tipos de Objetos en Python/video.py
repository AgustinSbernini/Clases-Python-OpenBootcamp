print("\n")
numero = 5
print("a tiene un valor de ", numero, " y su direccion de memoria es ", id(numero), " y es de tipo ",type(numero))
numero = 3.2
print("a tiene un valor de ", numero, " y su direccion de memoria es ", id(numero), " y es de tipo ",type(numero))
numero = 5
print("a tiene un valor de ", numero, " y su direccion de memoria es ", id(numero), " y es de tipo ",type(numero))
numero = 3.2
print("a tiene un valor de ", numero, " y su direccion de memoria es ", id(numero), " y es de tipo ",type(numero))
#TODO Inmutable datos esto quiere decir que las variables son inmutable por lo tanto no se pueden modificar. 
# Cambiar el valor hace que cambie la direccion de memoria.
print("\n")


tupla = ('a', '2', '3', 'd') #TODO Tuplas se hacen con ()
cadena = "hola mundo, COMO ESTAS"
print(tupla, cadena)
# tupla[0] = '2' cadena[0] = 'R' no se puede hacer porque son inmutables.
print("\n")


lista = ['b', "Roman", '1', 'z']
print(lista, id(lista))
lista[0] = 'h'
print("cambio b por h",lista, id(lista))
#TODO Lista se hacen con [], si se pueden modificar. No cambia la direccion de memoria
#TODO Objetos: En python todos los tipos de datos son objetos por lo tanto tienen metodos (funciones añadidas)
lista.append("Jorge") #Solo se puede apendear de a un tipo de dato
print("apendeo Jorge",lista, id(lista))
lista.remove('1') #Solo se puede remover de a un tipo de dato y tenes que decir exactamente cual dato vas a sacar
print("remuevo 1",lista, id(lista))
lista2 = ["america", "o",6.4,1]
lista.append(lista2) #TODO Sigue siendo un tipo de dato, en este caso otra lista, funciona raro hacer lista.append(lista)
print("apendeo lista2",lista,id(lista)) #Nunca cambio la direccion de memoria.
print("\n")


diccionario = { #Los diccionarios se hacen con {} y se decignan por clave: valor
    "clave": "valor",
    "Estornudo": 15,
    tupla: lista
}
diccionario[0] = 2
diccionario[1] = 6 #Se agrega al final como [clave] = valor. Raro.
print(diccionario)
popeado = diccionario.pop("Estornudo") #Elimina un elemento y lo devuelve por return
getteado = diccionario.get("clave") #Devuelve por return un elemento
print(diccionario)
print("Popeado: ",popeado, "getteado: ",getteado)
#TODO Diccionarios Se puede poner cualquier tipo de dato salvo una lista y diccionario como clave. Pero si como valor.
# Para modificar hay que seleccionar la clave.
print("\n")


conjuntos = {'a','b','a','b'} #TODO Set o Conjuntos no pueden tener valores duplicados a diferencia de las listas
print("muestra de conjuntos que no se repiten: ",conjuntos)
#TODO Operaciones matematicas
a = {0,2,5,6}
b = {1,2,3,4}

c = a | b #Union
print("Union de a con b ",c)
c = a & b #Interseccion
print("Interseccion de a con b ",c)
c = a - b  #Diferencia. Los que hay en a pero no en b
print("Diferencia de a con b ",c)
c = a ^ b #Diferencia simetrica. Los que no se repiten
print("Diferencia simetrica de a con b ",c)


print("\n")
#TODO Cadenas se hacen con =. cadena = "asd"
print("Imprimo cadena :", cadena)
print("Cadena capitalizada :", cadena.capitalize()) #Pone la primera mayuscula, resto minuscula
print("Cadena titulo :", cadena.title()) #Pone la todas las iniciales en mayuscula, resto minuscula
print("Cadena Minuscula :", cadena.lower()) #Pasa todo a minuscula
print("Cadena Mayuscula :", cadena.upper()) #Pasa todo a mayuscula
print("Cadena reemplaza :", cadena.replace('o','a')) #Reemplaza el primer elemento por el segundo elemento
print("Cadena cuenta repeticiones de letra:", cadena.lower().count('o'))
print("Cadena buscar :", cadena.find('mundo')) #Devuelve la posicion en la cadena donde esta ubicado el elemento -1 si no esta
print("Cadena transforma en lista :", cadena.split()) #Transforma la cadena en lista.
print("Combinacion de funciones en la cadena :", cadena.title().replace(',','').split())
lista = cadena.title().replace(',','').split()
print("Guardo la cadena en una lista :", lista)
cadena = '-'.join(lista) #Transforma la lista en cadena uniendolas por el elemento entre ' '.
print(cadena)
print("\n")


q = 2
e = 3
print("q elevado a la e, 2 elevado a la 3 = ",q ** e) #Operador de exponente
print("\n")


pedirDato = input("Lo que se va a pedir: ")
print(pedirDato)
print("\n")