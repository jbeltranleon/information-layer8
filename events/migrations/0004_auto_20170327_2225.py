# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170327_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='timezone',
            field=models.CharField(choices=[('America/Bogota', '(UTC-0500) America/Bogota'), ('other', 'other')], default='(UTC-0500) America/Bogota', max_length=255),
        ),
    ]
