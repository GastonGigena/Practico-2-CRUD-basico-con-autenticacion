from django import forms
from .models import Persona

from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['apellido', 'nombre', 'edad', 'oficina']
        widgets = {
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'value': 'Desconocido',
                'onfocus': "if(this.value=='Desconocido')this.value='';"
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'value': 'Desconocido',
                'onfocus': "if(this.value=='Desconocido')this.value='';"
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'value': '0',
                'onfocus': "if(this.value=='0')this.value='';"
            }),
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
