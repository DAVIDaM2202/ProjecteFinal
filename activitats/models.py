# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name="Nom del usuari")
    nom = models.CharField(max_length=50, blank=False, default='', verbose_name="Nom")
    cognom = models.CharField(max_length=50, blank=False, default='', verbose_name="Cognom")
    correu=models.EmailField(max_length=50, blank=False,default='', verbose_name="Correu electronic")
    def __str__(self):
        return self.user.get_username()

class Localitat(models.Model):
    nom = models.CharField(max_length=100, blank=False, default='',verbose_name="nom")
    latitud = models.CharField(max_length=100, blank=False, default='',verbose_name="latitud")
    longitud = models.CharField(max_length=100, blank=False, default='',verbose_name="longitud")
    def __str__(self):
        return self.nom
class Categoria(models.Model):
    nom = models.CharField(max_length=100, blank=False, default='',verbose_name="nom")
    def __str__(self):
        return self.nom

class Activitat(models.Model):
    nom = models.CharField(max_length=50, blank=False, default='', verbose_name="Nom")
    descripcio = models.TextField(max_length=500, blank=False, default='', verbose_name="Descripcio")
    dia = models.DateTimeField(max_length=100,verbose_name="Inici")
    #imatge = models.ImageField(upload_to='activitats/')
    diafinal = models.DateTimeField(max_length=100,verbose_name="Final")
    localitat = models.ForeignKey(Localitat,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creador = models.CharField(max_length=250, blank=False, default='', verbose_name="Nom")
    persones_inscrites = models.ManyToManyField(Persona, through='activitat_persones_inscrites')
    def __str__(self):
        return self.nom

class activitat_persones_inscrites(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    activitat = models.ForeignKey(Activitat, on_delete=models.CASCADE)
    assistira = models.CharField(max_length=2,blank=False, default='', verbose_name="assistira")

    class Meta:
        unique_together = (("persona", "activitat"),)
    def __str__(self):
            return '{0} esta inscrit a la activitat {1}'.format(self.persona.nom,self.activitat.nom)

class Comentari(models.Model):
    text = models.TextField(max_length=500, blank=False, default='', verbose_name="text")
    data = models.DateTimeField(max_length=100, default= timezone.now, verbose_name="data")
    persona = models.CharField(max_length=250, blank=False, default='', verbose_name="persona")
    id_activitat = models.ForeignKey(Activitat, verbose_name="idactivitat")
    def __str__(self):
        return self.persona