from django.contrib import admin

# Register your models here.
from galeriaproducto.models import producto, cita, portafolio

admin.site.register(producto)

class Datos(admin.ModelAdmin):
    list_display = ('nombre','telefono','asunto')

admin.site.register(cita,Datos)
admin.site.register(portafolio)
