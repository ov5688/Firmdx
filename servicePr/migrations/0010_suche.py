# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0009_auto_20170406_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suche', models.CharField(max_length=200, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
