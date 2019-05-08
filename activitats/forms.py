from django.forms import ModelForm, Select
from activitats.models import *
from django import forms


class registrePersona(ModelForm):
    nom_usuari = forms.CharField()
    contrasenya1 = forms.CharField()
    contrasenya2 = forms.CharField()

    class Meta:
        model = Persona
        fields = ["nom","cognom","correu"]
