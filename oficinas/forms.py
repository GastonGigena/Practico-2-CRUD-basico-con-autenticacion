from django import forms
from .models import Oficina

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = ['nombre', 'nombre_corto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_corto': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CargaMasivaOficinaForm(forms.Form):
    archivo = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv'}),
        help_text="Formato CSV: nombre,nombre_corto"
    )