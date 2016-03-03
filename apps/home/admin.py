from django.contrib import admin

# Register your models here.

from .models import Registro_docente
#Este es el registro Docentes
#Registrando el modelo en el administrador de django
# Register your models here.
class AdminRegistrado(admin.ModelAdmin):
	list_display = ['__str__','nombre','email']
	class Meta:
		model = Registro_docente

admin.site.register(Registro_docente,AdminRegistrado)