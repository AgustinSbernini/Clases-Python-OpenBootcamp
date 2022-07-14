#TODO Django es un framework (un conjunto de herramientas) que nos permite desarrollar sitios web de una forma mas rapido
# MTV utiliza el Model Template Vista, en lugar de usar MVC Model View Controller.
# Un Modelo es un objeto en Python. Tiene la representacion de los datos que tiene la base de datos.
# Vistas gestionan las peticiones que se le realizan a la pagina web. es lo que se encuentra despues del .com/
# Y se relaciona con los Templates que es el html final pero con codigo dentro. Es un html dinamico.

#TODO django-admin nombreProyecto .    Para poder crear un proyecto django hay que usar ese codigo para que te cree un paquete
# Donde va a estar guardado todos los modulos y ademas un proyecto.py
# Un proyecto esta compuesto por multiple aplicaciones que se manejan a traves de un mismo control administrativo
# Las aplicaciones tienen su codigo independiente en su propia carpeta.
# Todo lo generado por django tiene que guardarse en alguna base de dato. Por defecto en settings.py se ve que se configura
# Para usar con sqlite3. Ademas te trae un HTTP pequeño para probar, con python3 manage.py runserver. Localhost:8000

#TODO Aplicacion para crearla hay que ir a la consola al igual que con el django y pone 'python manage.py startapp nombreAPP'
# Ahora hay que conectar el proyecto principal con la aplicacion. Para eso hay que ir a settings del proyecto y buscar
# 'INSTALLED_APPS' y agregar la linea 'nombreAPP.apps.nombreAPPConfig', (importante , al final y las mayus)
# Luego hay que conectar la ruta (path) que aca se llaman Vista, para esto hay que ir a urls.py y agregar en urlpatterns
# path('nombreAPP/', include('nombreAPP.urls'))
# Error 'str' object has no attribute 'tag' = agregar en el import de django.urls import include (Te agrega otro por defecto)
# Error no module named 'nombreAPP.urls' = Crear en la aplicacion un fichero que se llame 'urls.py' y agregar la linea urlpatterns = []
# Ahora hay que migrar los cambios realizados con 'python manage.py migration' de esta forma se carga el db.sqlite3

#TODO Super Usuario es un usuario de administracion de django. Django tiene un panel de administracion y para acceder hay que ir
# Al puerto localhost:8000/admin donde te pide un usuario y contraseña. Estos se crean en python manage.py createsuperuser
# En este panel se podran ver los usuarios y los grupos creados.

#TODO Modelos(class) se crean dentro de las aplicaciones en el fichero models.py y tienen que heredar de (models.Model)
# UUIDField UUID es un generador de numero al azar que contiene 32 digitos en hexadecimal (unico)
# CharField contiene max_length 255 caracteres
# ForeignKey primer parametro de donde va a referenciarse
# TextField igual que CharField pero sin limite de caracteres
# ManyToManyField que puede tomar varias referencias desde la class referenciada
# DateField para guardar fechas.
# Opciones a poner: help_text Para dar un mensaje de guia, choices para elegir entre opciones, blank para dejar vacio el campo
# null para permitir que sea null, default para darle un valor por defecto, on_delete para setear un valor si se borra el campo

#TODO Admin.py (dentro de aplicacion) para permitir que el panel de administracion de django nos permita administrar los modelos 
# Dentro hay que importar from .models import nombreDeCadaModelo, separadoPorComa, todosLosModelos o podria ser con *
# Ahora hay que registrar los modelos en el panel de administracion con admin.site.register(cadaModelo)

#TODO URL para asignar hay que poner en urls.py en urlpatterns [re_path(r'^$', views.index, name = 'index')] que lo que quiere decir es
# r'^$' que mientras despues del nombreAPP/ no haya nada la pagina va a redireccionar a la funcion index del modulo views.
#from django.urls import re_path

#TODO Views hay que importar desde .models todos los modulos creados. Luego crear las funciones derivadas de request (peticiones)


#TODO Templates donde se crean los html
#TODO static/css donde se crean los styles.css


#TODO cuando se hace el migration y el makemigration va a ir generando archivos de manera secuencial para no repetir ejecuciones
# Solo los cambios realizados.