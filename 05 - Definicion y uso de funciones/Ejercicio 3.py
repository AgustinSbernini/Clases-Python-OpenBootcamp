# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def verificarAñoBisiesto(año):
    retorno = False
    año = int(año)
    if(año % 4 == 0):
        retorno = True
    return retorno

for i in range(0, 2022):
    añoBisiesto = verificarAñoBisiesto(i)
    if(añoBisiesto):
        print("El año",i,"es bisiesto")
