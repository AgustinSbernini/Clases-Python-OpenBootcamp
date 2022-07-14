#TODO Un modulo es un fichero en el disco duro que contiene una serie de sentencia y definiciones de python. Terminan en .py
# El modulo se suele llamar de la misma forma que el fichero (Modulo lo que tiene escrito, fichero donde se guarda)
# Para ejecutarlo en windows basta con hacer doble click
# Un modulo en Python es como una librería en C pero además de hacer el import para usar las funciones hay que acceder con .
# Paquetes son un conjunto de modulos dentro de un modulo
# Los modulos van a estar compuestos mayoritariamente de funciones y clases

from operaciones import operaciones as op # Se utiliza el as para darle un nombre
import operaciones.divisiones # Otra opcion para importar modulos podría usarse as
import pprint #Para ver mejor lo que se printea
#TODO import desde otra ruta. con import sys te importa todas los modulos que tengas en un path por defecto el programa.
# Si se quiere importar un modulo desde otro path hay que apendear el path a sys. sys.path.append("path").
# Para importar todo se usa from operaciones import * aunque para hacer esto hay que modificar el __init__ donde hay que
# escribirle __all__ = ['nombreDeCadaPaquete', 'paquete2'] los que no se escriban no van a importarse


def main():
    print()
    print(op.__name__, "\n")
    print(op.suma(4,7), "\n") # con el as se acorta en vez de poner operaciones.suma(x,x)

    print(operaciones.divisiones.divi(6,2), "\n") # Segunda forma
    divi = operaciones.divisiones.laDivision()
    resultado = divi.laDivi(8,3)
    print(resultado, "\n")

    print(2+op.PI,"\n")

    operador = op.Operador()
    print(operador.multiplicador(2,6), "\n")

    pprint.pprint(dir(operaciones)) # pprint para ver en fila y dir() para ver todas las funciones que tiene
    #TODO dir tambien se puede usar con lo que sea ya que todo es un objeto en Python dir(()), dir(5), dir([]), dir({}), dir('a')

    #TODO globals sirve para ver la tabla simbolos. Donde esta guardado todo lo que leyó el programa en ejecución. Es un diccionario.
    #TODO locals sirve para ver la tabla simbolos. Pero esta vez muestra lo que este dentro del scope donde se invoque.
    print("\n El resultado restado 2 desde el ambito local:",round(locals()['resultado'] - 2,2))




if __name__ == '__main__':
    main()