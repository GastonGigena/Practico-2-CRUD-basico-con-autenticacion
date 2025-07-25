from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})