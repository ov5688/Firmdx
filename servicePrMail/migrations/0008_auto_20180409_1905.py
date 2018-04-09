# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-09 19:05
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('servicePrMail', '0007_firmeneintrag_beschreibung'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmeneintrag',
            name='branche',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Umzug', 'Umzug'), ('Reinigung', 'Reinigung'), ('Maler', 'Maler'), ('Architekt', 'Architekt'), ('Sanitaer', 'Sanitaer'), ('Schreiner', 'Schreiner'), ('Gartenbau', 'Gartenbau'), ('Baufirma', 'Baufirma'), ('Immobilien', 'Immobilien')], max_length=80),
        ),
    ]