from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Formulariocita
from django.contrib import messages
import yagmail
from .models import portafolio

# Create your views here.
def home(request):  # primera vista
    return render(request, "index.html")
def Cita(request):
    if request.method == 'POST':
        form = Formulariocita(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Su cita ha sido agendada")
            
            # Obtener los datos del formulario
            nombre = form.cleaned_data.get('nombre') 
            email = form.cleaned_data.get('email')  
            asunto = form.cleaned_data.get('asunto')  
            fecha = form.cleaned_data.get('fecha_hora')

            # Configura yagmail con tu dirección de correo y contraseña de aplicación puede poner otro gmail si quieres
            yag = yagmail.SMTP('kayroabraham@gmail.com', 'npdolcpijanjslfc')  # Usa la contraseña de aplicación aquí

            # Enviar correo electrónico a tu dirección
            subject = 'Nueva Cita Agendada'
            message = f'Se ha agendado una cita:\n\nNombre: {nombre}\nEmail: {email}\nasunto: {asunto}\n fecha y hora:{fecha}'
            yag.send(to='kayroabraham@gmail.com', subject=subject, contents=message)  # Correo donde se enviara el email

            # Limpiar el formulario
            form = Formulariocita()
    else:
        form = Formulariocita()
    
    return render(request, 'formulario.html', {'form': form})

def Portafolio(request):
    items = portafolio.objects.all()
    return render(request, 'portafolio.html', {'items': items})

def detalles(request):
    return render(request, "detalles.html")

def contactos(request):
    return render(request, "contactos.html")
