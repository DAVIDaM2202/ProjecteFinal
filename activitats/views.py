# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate,login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from activitats.forms import registrePersona, User
from activitats.models import Persona
from django.urls import reverse


def index(request):
    return render(request,'activitats/index.html')
def pantallaInici(request):
    return render(request,'activitats/pantallaInicial.html')


def registre(request):
    print 'hola'
    form=registrePersona(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form_data = form.cleaned_data
            nom_usuari = form_data.get("nom_usuari")
            contrasenya1 = form_data.get("contrasenya1")
            contrasenya2 = form_data.get("contrasenya2")
            nom = form_data.get("nom")
            cognom = form_data.get("cognom")
            correu = form_data.get("correu")
            print (form_data)
            user = User.objects.create_user(nom_usuari, password=contrasenya1)
            user.save()
            persona = Persona.objects.create(user=user,nom=nom,cognom=cognom,correu=correu)
            persona.save()
            user1 = authenticate(username=nom, password=contrasenya1)
            login(request, user1)
            return HttpResponseRedirect(reverse('activitats:pantallaInici',))
    context = {
        "form": form,
    }
    return render(request, 'activitats/formulari.html', context)
