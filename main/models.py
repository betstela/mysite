from django.db import models

# Create your models here.
class cursos(models.Model):
    redes=models.CharField(max_length=30)
    matematicas=models.CharField(max_length=30)
    informatica=models.CharField(max_length=30)
    literatura=models.CharField(max_length=30)


def __str__(self):
    return self.nombre
