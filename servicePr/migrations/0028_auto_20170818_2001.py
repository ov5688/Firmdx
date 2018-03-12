# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-18 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0027_auto_20170818_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firma',
            name='geo',
        ),
        migrations.AddField(
            model_name='geo',
            name='firm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='servicePr.Firma'),
            preserve_default=False,
        ),
    ]
