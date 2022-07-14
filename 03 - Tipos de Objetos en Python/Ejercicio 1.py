#Para este ejercicio tenéis que crear en la consola de python variables que representen los siguientes datos de un contacto:
#Nombre
#Apellidos
#Edad
#Email
#Teléfono
#Casado (verdadero o falso)
#Con Hijos (verdadero o falso)
#Lista de amigos
#Películas vistas (diccionario con clave y valor. El valor será el título de la película)
#Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().
#Tienes que subir capturas de pantalla en una carpeta comprimida zip.

nombre = "Agustin"
apellido = "Sbernini"
edad = 24
email = "agus.sbernini@gmail.com"
telefono = 15448877
casado = False
conHijos = False
listaDeAmigos = ["Juan","Gabriel","Daniel","Esteban"]
peliculas = {
    "peli1" : "Dracula",
    "peli2" : "El señor de los anillos",
    "peli3" : "Harry Potter"
}
print("\n\n")
print(nombre,apellido, " de ", edad, " anios de email ", email, " es casado? ", casado, " tiene hijos? ", conHijos)
print("\nLas peliculas que vió fue:", peliculas.get("peli1"),",", peliculas.get("peli2"),"y", peliculas.get("peli3"),
"con sus amigos ", ' '.join(listaDeAmigos), "\n\n")