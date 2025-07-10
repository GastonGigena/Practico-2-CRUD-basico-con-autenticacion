from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['apellido', 'nombre', 'edad', 'oficina']
        widgets = {
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'oficina': forms.Select(attrs={'class': 'form-control'}),
        }

class CargaMasivaPersonaForm(forms.Form):
    archivo = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv'}),
        help_text="Formato CSV: apellido,nombre,edad,oficina_id"
    )
    
from django import forms

class CargaMasivaPersonasForm(forms.Form):
    archivo = forms.FileField(label="Archivo CSV")
