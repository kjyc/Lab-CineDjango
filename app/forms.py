"""
Definition of forms.
"""

from django import forms
from app.models import Pelicula
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RegistroForm(forms.Form): #Formulario de registro de usuarios
    username = forms.EmailField(required=True) #email
    pass1 = forms.CharField(widget=forms.PasswordInput) #Pass
    pass2 = forms.CharField(widget=forms.PasswordInput) #Pass repetido
class PeliculaForm(forms.ModelForm):
        class Meta:
            model = Pelicula
            fields = ('titulo','direccion','anio','genero','sinopsis','votos', 'imagen')
            widgets = {
                'titulo' : forms.TextInput(attrs={'class':'form-control'}),
                'direccion' : forms.TextInput(attrs={'class':'form-control'}),
                'anio' : forms.NumberInput(attrs={'class':'form-control'}),
                'genero' : forms.TextInput(attrs={'class':'form-control'}),
                'sinopsis' : forms.TextInput(attrs={'class':'form-control'}),
                'votos' : forms.NumberInput(attrs={'class':'form-control'}),
                'imagen' : forms.FileInput(attrs={'class': 'form-control-file'})
                }
class VotoForm(forms.Form):
        todasLasPeliculas = forms.ModelChoiceField(queryset=Pelicula.objects.all(), empty_label="- Selecciona -", widget = forms.Select(attrs={'class':'form-control'}))
       
class GeneroForm(forms.Form):
    CHOICES = Pelicula.objects.values_list('genero', 'genero').distinct()
    todosLosGeneros = forms.ChoiceField(choices=CHOICES, widget = forms.Select(attrs={'class':'form-control'}))