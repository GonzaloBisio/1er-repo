from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
            return '{}'.format(self.nombre)