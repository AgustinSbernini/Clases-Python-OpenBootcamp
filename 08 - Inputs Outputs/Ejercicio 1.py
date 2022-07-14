# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. 
# Para ello, tendréis que acceder dos veces al archivo creado.
f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs.py\\archivo.txt",'w')
f.write("Estoy dentro del archivo\n")
f.close()

f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs.py\\archivo.txt", 'a+')
f.write("Volvi a entrar al archivo\n")
f.close()

f = open("C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\8 - Inputs Outputs.py\\archivo.txt", 'r')
lineasDelTexto = f.readlines()
for linea in lineasDelTexto:
    print (linea)
f.close()