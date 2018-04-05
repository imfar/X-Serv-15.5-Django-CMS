from django.db import models
# Create your models here.

class Recurso(models.Model):
    name = models.CharField(max_length=128)
    contenido = models.TextField(default="")
    def __str__(self):
	    return self.name
