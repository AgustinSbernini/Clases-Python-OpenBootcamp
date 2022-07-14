#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros)
#calcule el índice de masa corporal y lo almacene en una variable e imprima por pantalla la frase
#Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. 
# ienes que subir capturas de pantalla en una carpeta comprimida zip.

print("\n\nPara poder calcular su indice de masa corporal se necesita saber el peso y la estatura de la persona.")
peso = input("Ingrese su peso por favor: ")
estatura = input("Ingrese su estatura por favor: ")
indiceMasaCorporal = round((float(peso) / (float(estatura)**2)),2)
print("Su indice de masa corporal es de: ", indiceMasaCorporal)
print("\n\n")