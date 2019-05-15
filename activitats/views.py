# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json

from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from activitats.forms import registrePersona, User, formActivitats
from activitats.models import Persona
from django.urls import reverse
from activitats.models import Activitat,Localitat

def index(request):
    return render(request,'activitats/index.html')
@login_required

def pantallaInici(request):
    form = formActivitats(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form_data = form.cleaned_data
            nom = form_data.get("nom")
            descripcio = form_data.get("descripcio")
            dia = form_data.get("dia")
            diafinal = form_data.get("diafinal")
            localitat = form_data.get("localitat")
            categoria = form_data.get("categoria")
            creador = str(request.user.get_username())
            print (form_data)
            activitat = Activitat.objects.create(nom=nom,descripcio=descripcio,dia=dia,diafinal=diafinal,localitat=localitat,categoria=categoria,creador=creador)
            activitat.save()

            return HttpResponseRedirect(reverse('activitats:pantallaInici', ))
    context = {
        "form": form,
    }
    return render(request, 'activitats/pantallaInicial.html', context)


def editarActivita(request, id_activitat= None):
    if id_activitat:
        activitat = get_object_or_404(Activitat, pk=id_activitat)

    else:
        activitat = Activitat()
    if request.method == 'POST':
        form = formActivitats(request.POST, initial={'dia': datetime.date.today()}, instance=activitat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('activitats:pantallaInici'))

    else:
        form = formActivitats(initial={'dia': datetime.date.today()}, instance=activitat)

    context = {'form': form}
    return render(request, 'activitats/editarActivitat.html', context)


def registre(request):
    form=registrePersona(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form_data = form.cleaned_data
            nom_usuari = form_data.get("nom_usuari")
            contrasenya1 = form_data.get("contrasenya1")
            nom = form_data.get("nom")
            cognom = form_data.get("cognom")
            correu = form_data.get("correu")
            user = User.objects.create_user(nom_usuari, password=contrasenya1)
            user.save()

            persona = Persona.objects.create(user=user,nom=nom,cognom=cognom,correu=correu)
            persona.save()
            user1 = authenticate(username=nom, password=contrasenya1)
            login(request, user1,backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse('activitats:pantallaInici',))
    context = {
        "form": form,
    }
    return render(request, 'activitats/formulari.html', context)



'''def ensenyar (request):
    print("hola")
    return render(request,'activitats/pantallaInicial.html')'''


def ensenyar(request):
    if request.method == "GET":
        activitats = Activitat.objects.all()
        llista = [ serializer(activitat) for activitat in activitats ]
        return HttpResponse(json.dumps(llista), content_type='aplication/json')
    HttpResponseRedirect(reverse('Index'))

def serializer(activitat):
    dia = str(activitat.dia)
    diafinal = str(activitat.diafinal)

    return {'id':activitat.id,'nom': activitat.nom,'descripcio': activitat.descripcio,'dia':dia,'diafinal':diafinal,'localitat':activitat.localitat.nom,'categoria': activitat.categoria.nom
        }

def activitatsPropies(request):
    nom = Q(creador= str(request.user.get_username()))
    print nom
    activitats = Activitat.objects.filter(nom)
    print activitats
    context = {
        "activtats": activitats,
    }
    return render(request, 'activitats/lesMevesActivitats.html', context)


def apiLocalitats(request):
    nom = request.GET.get('term', '')
    pagina = int( request.GET.get('page', 0))
    maxim = 10
    filtro_nombre = Q(nom__icontains = nom)
    resultado_filtro = Localitat.objects.filter(filtro_nombre)
    lista = [{"text": "{0}".format(x.nom.encode('utf-8'))}
        for x in resultado_filtro[int(pagina) * maxim : (int(pagina) * maxim)+ maxim]]
    response ={}
    response['pagination']={'more': len(lista) == maxim}
    response['results'] = lista
    return HttpResponse(json.dumps(response), content_type="application/json")

def activitatDetallada(request, id_activitat):
    activitat=get_object_or_404(Activitat,pk=id_activitat)
    return render(request, 'activitats/informacioActivitats.html',{'activitat':activitat})
