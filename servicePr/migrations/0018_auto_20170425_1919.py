# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0017_auto_20170425_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architekt',
            name='firm_plz',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='baufirma',
            name='firm_plz',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='catering',
            name='firm_plz',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gartenbau',
            name='firm_plz',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='immobilien',
            name='firm_plz',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reinigung',
            name='firm_plz',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sanitaer',
            name='firm_plz',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_plz',
            field=models.IntegerField(null=True),
        ),
    ]