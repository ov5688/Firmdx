# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-12 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0022_remove_offertanfrage_selected_firmen'),
    ]

    operations = [
        migrations.AddField(
            model_name='architekt',
            name='firm_beschreibung',
            field=models.CharField(db_index=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='baufirma',
            name='firm_beschreibung',
            field=models.CharField(db_index=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='catering',
            name='firm_beschreibung',
            field=models.CharField(db_index=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='gartenbau',
            name='firm_beschreibung',
            field=models.CharField(db_index=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='immobilien',
            name='firm_beschreibung',
            field=models.CharField(db_index=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='maler',
            name='firm_beschreibung',
            field=models.CharField(db_index=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='reinigung',
            name='firm_beschreibung',
            field=models.CharField(db_index=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='sanitaer',
            name='firm_beschreibung',
            field=models.CharField(db_index=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='schreiner',
            name='firm_beschreibung',
            field=models.CharField(db_index=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='architekt',
            name='firm_adress',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='architekt',
            name='firm_homepage',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='architekt',
            name='firm_name',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='architekt',
            name='firm_ort',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='architekt',
            name='firm_plz',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='baufirma',
            name='firm_plz',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='catering',
            name='firm_plz',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gartenbau',
            name='firm_plz',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='immobilien',
            name='firm_plz',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='maler',
            name='firm_plz',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='reinigung',
            name='firm_adress',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='reinigung',
            name='firm_homepage',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='reinigung',
            name='firm_logo',
            field=models.ImageField(db_index=True, upload_to=b'treasure_images'),
        ),
        migrations.AlterField(
            model_name='reinigung',
            name='firm_name',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='reinigung',
            name='firm_ort',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='reinigung',
            name='firm_plz',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sanitaer',
            name='firm_plz',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='schreiner',
            name='firm_plz',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_adress',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_beschreibung',
            field=models.CharField(db_index=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_homepage',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_ort',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_plz',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]