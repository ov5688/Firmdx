# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-18 20:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0028_auto_20170818_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offertenanfrage',
            name='branche',
        ),
        migrations.DeleteModel(
            name='OffertenAnfrage',
        ),
    ]
