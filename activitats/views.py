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

from activitats.forms import registrePersona, User, formActivitats, editPersona
from activitats.models import Persona
from django.urls import reverse
from activitats.models import Activitat,Localitat,activitat_persones_inscrites,Comentari

def index(request):
    return render(request,'activitats/index.html')
@login_required
def pantallaInici(request):
    form = formActivitats(request.POST or None)
    x = Persona.objects.get(user=request.user)
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
        "persona":x,
    }
    return render(request, 'activitats/pantallaInicial.html', context)

##########################EDITAR ACTIVITAT#############################
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

########################## EDITAR PERFIL ##############
def editarPerfil(request, id_persona):
   persona = Persona.objects.all().filter(pk=id_persona)[0]
   print (persona.user.password)
   form = editPersona(request.POST or None, initial={"nom":persona.nom,"cognom":persona.cognom,"correu":persona.correu,"nom_usuari":persona.user.username})
   if request.method == 'POST':
       if form.is_valid():
           form_data = form.cleaned_data
           nom = form_data.get("nom")
           cognom = form_data.get("cognom")
           correu = form_data.get("correu")
           Persona.objects.filter(pk=id_persona).update(nom=nom,cognom=cognom,correu=correu)
           return HttpResponseRedirect(reverse('activitats:pantallaInici', ))

   context = {
        "form": form,
    }
   return render(request,'activitats/editarPersona.html',context)

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


######################### INSCRIURES ###############################
def inscriures (request):
    personaobject= Persona.objects.get(user=request.user)
    activitatobject= Activitat.objects.get(pk= request.POST.get('activitat'))
    activitats_inscrits= activitat_persones_inscrites.objects.filter(persona=personaobject,activitat=activitatobject,assistira='1').count()
    if (activitats_inscrits == 0):
        x = activitat_persones_inscrites.objects.create(persona=personaobject,activitat=activitatobject,assistira='1')
        x.save()
        print 'incrit'
    else:
        activitat_persones_inscrites.objects.get(persona=personaobject, activitat=activitatobject, assistira='1').delete()
        print 'desinscrit'
    return render(request,'activitats/informacioActivitats.html' )

#########################################Ensenyar activitats###############################
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
############################################Comentaris########################################
def comentaris(request):
    if request.method == "GET":
        id = request.GET.get('busca')
        activitat = Activitat.objects.get(pk = id)
        comentaris = Comentari.objects.filter(id_activitat = activitat)
        llista = [ serializer1(comentari) for comentari in comentaris ]
        return HttpResponse(json.dumps(llista), content_type='aplication/json')
    HttpResponseRedirect(reverse('Index'))

def serializer1(comentari):
    data = str(comentari.data)
    return {'textt':comentari.text,'dataa': data,'persona': comentari.persona
        }

def crearComentari(request):
    textrebut=  request.POST.get('text')
    activitatobject= Activitat.objects.get(pk= request.POST.get('activitat'))
    x = Comentari.objects.create(text=textrebut,persona=request.user,id_activitat=activitatobject)
    return render(request,'activitats/informacioActivitats.html' )



############################################Les meves activitats###################3
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
    personaobject = Persona.objects.get(user=request.user)
    activitatobject = Activitat.objects.get(pk=id_activitat)
    activitats_inscrits = activitat_persones_inscrites.objects.filter(persona=personaobject,activitat=activitatobject,assistira='1').count()
    if (activitats_inscrits > 0):
        text = '1'
        context = {
            "activitat":activitat,
            "jaestasinscrit": text,
        }
        return render(request, 'activitats/informacioActivitats.html', context)
    text = '0'
    context = {
        "activitat": activitat,
        "jaestasinscrit": text,
    }
    return render(request, 'activitats/informacioActivitats.html',{'activitat':activitat})
