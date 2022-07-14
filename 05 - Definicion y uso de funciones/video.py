#TODO funciones se declaran con def nombreFuncion(): se puede poner o no parametros, se puede poner o no return.
# Se invoca como nombreFuncion() 
# Se puede definir otra funcion dentro de una funcion pero solo se puede usar ahi mismo

temperatura = 12

def nombre():
    global temperatura #TODO global sirve para modificar variables que esten fuera de la funcion
    temperatura = 6
    print("La temperatura es:",temperatura)

print("\n")
nombre()
print("La temperatura es:",temperatura)
print("\n")


#TODO parametros opcionales se igualan al valor que tendran si no se los declaran en el llamado de la funcion
# Puede haber todos los parametros opcionales que se quiera. Siempre tienen que ser los ultimos dentro de los parametros.
# No podria declararse como parametro opcional el primer elemento y el resto no.
def suma(a, b = 4, c = 2): 
    print("La suma es:",a + b + c)

suma(2)
suma(2,2)
suma(2,2,7)
suma(c = 9, a = 1) #Se le puede dar los valores en el orden que se quiera mientras se los declaren.
print("\n")


#TODO parametros variables por convención se pone *args y lo que se ingrese se convierte en tupla
def sumatoria(*args):
    resultado = 0
    print("La tupla formada es:",args)
    for arg in args:
        resultado += arg

    return resultado

print("La sumatoria es:", sumatoria(3,4,2,1,5))
print("\n")


#TODO parametros con nombres cambiantes por convención se pone **kwargs y lo que se Ingrese se convierte en un diccionario
def diccionario(**kwargs):
    print("El diccionario formado es:", kwargs)
    for key, value in kwargs.items():
        print("Tu",key,"es", value)

diccionario(vivienda = "Casa", vehiculo = "Auto", estadoCivil = "Casado")
def otroSumatoria(**kwargs):
    inicial = kwargs['inicial'] if 'inicial' in kwargs else 1
    final = kwargs['final'] if 'final' in kwargs else inicial #TODO operador terciario del if. Equivalente a ? en otros lenguajes
    resultado = 0
    for i in range(inicial, final + 1):
        resultado += i
    return resultado

print("El resultado de la otra sumatoria es:", otroSumatoria(final = 3))
print("\n")

#TODO return varios se guardan todos juntos en una sola variable como tupla o se guardan en distintas variables definidas
# Consecutivamente, donde el numero de variables tiene que ser igual al numero de return
def operaciones(a,b):
    return a+b,a-b,a*b

resultado = operaciones (2,4)
print("El resultado de todas las operaciones es:",resultado)
print("Otra manera de imprimir es:", resultado[2])
laSuma, laResta, laMultiplicacion = operaciones (2,4)
print("La suma es:", laSuma, "La Resta es:",laResta, "la Multiplicacion es:",laMultiplicacion, "\n\n")


#TODO Lambda funciones anonimas no poseen nombres y se las asigna a una varible. El codigo debe estar escrito en una sola linea
# Los parametros se agregan despues del lambda separados por ,
# Aplica los parametros opcionales
anonima = lambda nombre, nombre2 = "perez": print("el primer nombre ingresado es:",nombre,"y el segundo es:", nombre2)
anonima("Juan") 
print("\n")