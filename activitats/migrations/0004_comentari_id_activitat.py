# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-17 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitats', '0003_auto_20190517_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentari',
            name='id_activitat',
            field=models.CharField(default='', max_length=5, verbose_name='idactivitat'),
        ),
    ]
