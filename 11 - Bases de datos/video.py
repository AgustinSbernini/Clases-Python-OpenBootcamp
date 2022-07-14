#TODO Bases de datos relacionales relacionan unas tablas con otras. las filas tienen nombres y contienen datos en su interior 
# Que pueden ser modificadas.
 
#TODO SQLite es una base de datos que se suele usar para proyectos pequeños ya que utiliza pocos recursos pero por el mismo motivo
# No puede almacenar una gran cantidad de datos, ni puede accederse a un mismo fichero desde dos o mas programas a la vez
# Esta base de datos se guarda en nuestro pc, no esta conectado al internet.

import getpass
import sqlite3
#TODO Conectarse a la base de datos para poder usarla. Similar a open para los files
# Con isolation_level = None hace que los comandos se commiteen automaticamente al ejecutarlos
# Caso contrario deberia hacerse un conn.commit() al finalizar el programa para que se manden los datos al servidor
base = 'C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\11 - Bases de datos\\primeraBaseDeDatos.db'
conn = sqlite3.connect(f'{base}', isolation_level = None)

#TODO Cursor sirve para enviarle comandos a la base de datos. Almacena los datos por donde se puede iterar.

cursor = conn.cursor()

#cursor.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL) ')

# cursor.execute('INSERT INTO usuarios VALUES (1, "Agus", "contraAgus")')
# cursor.execute('INSERT INTO usuarios VALUES (2, "Nicky", "contraNicky")')
# cursor.execute('INSERT INTO usuarios VALUES (3, "Juan", "contraJuan")')
# cursor.execute('INSERT INTO usuarios VALUES (5, "Fer", "contraFer")')
# cursor.execute('INSERT INTO usuarios VALUES (6, "Salvar", "contraSalvar")')

rows = cursor.execute('SELECT * FROM usuarios')

for row in rows:
    print(row)

def comprobacionUsuario(usuario, password):
    row = cursor.execute(f'SELECT id FROM usuarios WHERE username = "{usuario}" AND password = "{password}"')
    data = row.fetchone()

    if(data == None):
        retorno = False
    else:
        retorno = True
    
    return retorno

if comprobacionUsuario("Agus", "contraaAgus"):
    print("Log in correcto")
else:
    print("Log in incorrecto")


def crearUsuario(id, username, password):
    cursor.execute(f'INSERT INTO usuarios (id, username, password) VALUES ({id},"{username}", "{password}")')

id = input("Ingrese el id: ")
username = input("Username: ")
password = getpass.getpass("Password: ")

crearUsuario(id, username, password)

#TODO Cerrar la coneccion al terminar el programa. similar al close para los files.
cursor.close()
conn.close()