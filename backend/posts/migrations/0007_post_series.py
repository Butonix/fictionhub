# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-10 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_auto_20170610_0214'),
        ('posts', '0006_auto_20170610_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='series',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='series.Series'),
        ),
    ]
