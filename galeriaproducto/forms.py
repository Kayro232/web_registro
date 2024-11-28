from django import forms
from .models import cita

class Formulariocita(forms.ModelForm):
    class Meta:
        model = cita
        fields = ['nombre','email','telefono','asunto','fecha_hora']
        widgets = {
            'fecha_hora':forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }