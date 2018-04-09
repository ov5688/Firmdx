# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from servicePr.models_new import Branchen
from multiselectfield import MultiSelectField

class OffertenAnfrage(models.Model):
    name = models.CharField(db_index=True, max_length=200, null=True)
    plz = models.IntegerField(db_index=True)
    ort = models.CharField(db_index=True, max_length=200, null=True)
    tel = models.CharField(db_index=True, max_length=200, null=True)
    beschreibung = models.TextField()
    eMail = models.EmailField(db_index=True, max_length=200, null=True)
    send = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.eMail + ' - ' + str(self.timestamp)

class TempEMail(models.Model):
    tempMail = models.EmailField(db_index=True, max_length=200, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return self.tempMail + ' updated: ' + str(self.updated) + ' timestamp: ' + str(self.timestamp)

class Firmeneintrag(models.Model):
    BRANCHEN = (
        ('Umzug', 'Umzug'),
        ('Reinigung', 'Reinigung'),
        ('Maler', 'Maler'),
        ('Architekt', 'Architekt'),
        ('Sanitaer', 'Sanitaer'),
        ('Schreiner', 'Schreiner'),
        ('Gartenbau', 'Gartenbau'),
        ('Baufirma', 'Baufirma'),
        ('Immobilien', 'Immobilien'),
    )

    branche = MultiSelectField(choices=BRANCHEN)
    name = models.CharField(db_index=True, max_length=200, null=True)
    firma = models.CharField(db_index=True, max_length=200, null=True)
    plz = models.IntegerField(db_index=True)
    ort = models.CharField(db_index=True, max_length=200, null=True)
    tel = models.CharField(db_index=True, max_length=200, null=True)
    eMail = models.EmailField(db_index=True, max_length=200, null=True)
    beschreibung = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.eMail + ' - ' + str(self.timestamp)
