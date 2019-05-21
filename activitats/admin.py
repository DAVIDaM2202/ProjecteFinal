# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from activitats.models import Persona,Activitat,Categoria,Localitat,activitat_persones_inscrites, Comentari

admin.site.register(Persona)
admin.site.register(Activitat)
admin.site.register(Categoria)
admin.site.register(Localitat)
admin.site.register(activitat_persones_inscrites)
admin.site.register(Comentari)




