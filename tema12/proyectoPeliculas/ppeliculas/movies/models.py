from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.apellido}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    sinopsis = models.TextField(max_length=1000, help_text="resumen de la pelicula")
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'