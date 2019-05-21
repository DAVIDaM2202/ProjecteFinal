# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-17 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=500, verbose_name='text')),
                ('data', models.DateTimeField(max_length=100, verbose_name='data')),
                ('persona', models.CharField(default='', max_length=250, verbose_name='Nom')),
            ],
        ),
    ]