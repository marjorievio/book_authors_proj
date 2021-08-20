from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    desc = models.TextField(max_length=255) 
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Title: {self.title}"


class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(max_length=255, null=True, blank=True)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name

    def __repr__(self):
        return f"Nombre: {self.first_name} | Apellido: {self.last_name}"

# python manage.py makemigrations
# python manage.py migrate
# from books_authors_app.models import *
# c_sharp=Book.objects.create(title="C Sharp",desc="Lenguaje de Programación de Microsoft")
# java=Book.objects.create(title="Java",desc="Lenguaje de Programación")                        
# python=Book.objects.create(title="Python",desc="Otro Lenguaje de Programación")
# php=Book.objects.create(title="PHP",desc="Procesador de HyperText")                                 
# ruby=Book.objects.create(title="Ruby",desc="Otro lenguaje de programación más")

# jane_a=Author.objects.create(first_name="Jane",last_name="Austen")      
# emily_d=Author.objects.create(first_name="Emily",last_name="Dickinson")       
# fyodor_d=Author.objects.create(first_name="Fyodor",last_name="Dostoevksy")         
# william_s=Author.objects.create(first_name="William",last_name="Shakespeare")           
# lau_t=Author.objects.create(first_name="Lau",last_name="Tsu")

# c_sharp.title="C #"
# c_sharp.save()

# william_s.first_name="Bill"
# william_s.save()

# william_s.first_name

# jane_a.books.add(c_sharp)           
# jane_a.books.add(java)

# jane_a.books.all()               PARA HACER LA CONSULTA

# emily_d.books.add(c_sharp,java,python)

# fyodor_d.books.add(c_sharp,java,python,php)

# william_s.books.add(c_sharp,java,python,php,ruby)

# python.authors.all()

# python.authors.remove(emily_d)

# java.authors.add(Author.objects.all()[4])

# fyodor_d.books.all()

# ruby.authors.all()



