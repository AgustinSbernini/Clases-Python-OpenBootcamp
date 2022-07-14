# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, 
# la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

base = 'C:\\Users\\flias\\Visual Studio Code Workspace\\Clases-Python-OpenBootcamp\\11 - Bases de datos\\primeraBaseDeDatos.db'
conn = sqlite3.connect(f'{base}', isolation_level = None)
cursor = conn.cursor()

cursor.execute('CREATE TABLE Alumno (id INTEGER PRIMARY KEY, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL)')

cursor.execute('INSERT INTO Alumno (id, name, surname) VALUES (1, "Esteban", "Gomez")')
cursor.execute('INSERT INTO Alumno (id, name, surname) VALUES (2, "Jose", "Perez")')
cursor.execute('INSERT INTO Alumno (id, name, surname) VALUES (3, "Daniel", "Lopez")')
cursor.execute('INSERT INTO Alumno (id, name, surname) VALUES (4, "Pedro", "Alonso")')
cursor.execute('INSERT INTO Alumno (id, name, surname) VALUES (5, "Julian", "Odera")')
cursor.execute('INSERT INTO Alumno (id, name, surname) VALUES (6, "Mateo", "Lopez")')
cursor.execute('INSERT INTO Alumno (id, name, surname) VALUES (7, "Bautista", "Burgos")')
cursor.execute('INSERT INTO Alumno (id, name, surname) VALUES (8, "Leandro", "Morandi")')

alumnoBuscado = cursor.execute('SELECT * FROM Alumno WHERE name = "Julian"').fetchone()

print(alumnoBuscado)

cursor.close()
conn.close()