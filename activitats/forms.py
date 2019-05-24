import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select
from activitats.models import *
from django import forms
from bootstrap3_datetime.widgets import DateTimePicker



class registrePersona(ModelForm):
    nom_usuari = forms.CharField()
    contrasenya1 = forms.CharField(widget=forms.PasswordInput)
    contrasenya2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Persona
        fields = ["nom","cognom","correu"]
    def clean(self):
        password = self.cleaned_data['contrasenya1']
        confirm_password = self.cleaned_data['contrasenya2']
        nom_usuari = self.cleaned_data['nom_usuari']
        user = User.objects.filter(username=nom_usuari).count()
        if user > 0:
            raise ValidationError("El usuari ja existeix")
        if password != confirm_password:
            raise ValidationError("No coincideixen les contrasenyes")

class editPersona(ModelForm):
    class Meta:
        model = Persona
        fields = ["nom","cognom","correu"]

class formActivitats(ModelForm):
    class Meta:
        model = Activitat
        fields = ["nom","descripcio","dia","diafinal","localitat","categoria"]
        widgets = {'dia': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}),
                   'diafinal': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm" }),
                   'localitat': Select(attrs={'class': 'localitat','style':'width: 100% !important'})
                   }
    def clean(self):
        dia = self.cleaned_data['dia']

        diafinal = self.cleaned_data['diafinal']
        print diafinal.day
        if diafinal < dia:
            print 'entra'
            raise ValidationError("No pots ficar una data mes petita, corregeix l'activitat")
        #        if dia.day < diafinal.day and dia.month >= diafinal.month:
