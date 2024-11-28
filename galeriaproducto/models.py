from django.db import models

# Create your models here.
class producto(models.Model):
    nombre=models.CharField(max_length=30) #almacena texto
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField() #almacena numeros

class cita(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField(unique=False)
    telefono = models.CharField(max_length=8)  # Cambiado a CharField y se define max_length
    asunto = models.CharField(max_length=100) 
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return self.nombre
    
class portafolio(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='portafolio/')
    descripcion = models.TextField()


    def __str__(self):
        return self.titulo