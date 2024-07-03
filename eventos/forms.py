from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario, Evento


class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico', required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su correo electrónico'
    }))

    nombre = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su nombre'
    }))

    password1 = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su contraseña'
    }))

    password2 = forms.CharField(label='Confirmar Contraseña', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirme su contraseña'
    }))

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo Electrónico',
        'autofocus': True
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña'
    }))


class EventoForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.SelectDateWidget)
    hora = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'ubicacion', 'fecha', 'hora']
