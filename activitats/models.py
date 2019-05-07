# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Nom del usuari")
    nom = models.CharField(max_length=100, blank=False, default='', verbose_name="Nom")
    cognom = models.CharField(max_length=100, blank=False, default='', verbose_name="Cognom")
    correu=models.EmailField(max_length=100, blank=False,default='', verbose_name="Correu electronic")
