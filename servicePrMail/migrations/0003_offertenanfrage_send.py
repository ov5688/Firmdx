# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicePrMail', '0002_firmeneintrag'),
    ]

    operations = [
        migrations.AddField(
            model_name='offertenanfrage',
            name='send',
            field=models.TextField(null=True),
        ),
    ]
