import uuid
from django.db import models
from django.urls import reverse

class Gender(models.Model):
    name = models.CharField(max_length = 64, help_text = "Inserte el nombre del genero")
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length = 32) # CharField hasta 255 caracteres
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null=True) # On delete hace que si se borra la ForeignKey
    # El campo queda en NULL en lugar de borrarse el libro. Y Permitimos que pueda tomar el valor NULL. 'Author' es de donde toma la referencia
    summary = models.TextField(max_length = 100, help_text = "De que se trata el libro?") # TextField tiene capacidad ilimitada
    isbn = models.CharField('ISBN',max_length = 13, help_text = "El ISBN de 13 caracteres")
    gender = models.ManyToManyField(Gender) # Puede estar relacionado con varios generos

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args = [str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "ID unico para este libro")
    # UUID es un generador de numero al azar que contiene 32 digitos en hexadecimal (probabilidad de repetir 1 en 600 billon)
    book = models.ForeignKey('Book', on_delete = models.SET_NULL, null = True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null = True, blank = True) # Retorno de fecha cuando fue alquilado

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length = 1, choices = LOAN_STATUS, blank = True, default = 'm', help_text = 'Disponibilidad del libro')

    class Meta:
        ordering = ["due_back"]

    def __str__(self) -> str:
        return (f'{self.id}, {self.book.title}')

class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null = True, blank = True)
    date_of_death = models.DateField('Died', null = True, blank = True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return (f'{self.last_name}, {self.first_name}')
