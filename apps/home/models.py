from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registro_docente(models.Model):
	nombre = models.CharField(max_length=200,blank=True, null=True)
	email = models.EmailField()
	codigo_postal=models.IntegerField(blank=True , null = True)
	registro =models.DateTimeField(auto_now_add=True , auto_now = False)
	actualizado = models.DateTimeField(auto_now_add= False , auto_now = True)

	def __str__(self):
		return self.nombre