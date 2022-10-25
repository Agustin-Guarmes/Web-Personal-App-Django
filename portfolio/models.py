from pyexpat import model
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.
class Project(models.Model):    #esta clase va a representar la tabla(relacional) de mi BBDD
    title = models.CharField(max_length=200, verbose_name = "Título")   #char es un campo de caracteres
    description = models.TextField(verbose_name = "Descripción")        #este es otro campo de mi BBDD y es de tipo texto
    image = models.ImageField(verbose_name = "Imagen", upload_to = "projects")
    link = models.URLField(verbose_name = "Dirección web", null = True, blank = True)
    created = models.DateTimeField(auto_now_add =True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now =True, verbose_name = "Fecha de modificación")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "proyecto"   #para que me traduzca project y projects
        verbose_name_plural = "proyectos"
        #como quiero que vayan del proyecto más nuevo al mas viejo hago lo siguiente
        ordering = ["-created"]     #para ordenar de la fecha más nueva a la más antigua