# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-22 02:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicePr', '0031_auto_20170818_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lan', models.CharField(db_index=True, max_length=200, null=True)),
                ('lat', models.CharField(db_index=True, max_length=200, null=True)),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicePr.Firma')),
            ],
        ),
    ]
