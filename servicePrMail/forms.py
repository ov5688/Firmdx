from django import forms
from servicePrMail.models import OffertenAnfrage, Firmeneintrag

class EintragFormular(forms.ModelForm):
    class Meta:
        model = Firmeneintrag
        fields = ['firma', 'name', 'plz', 'ort', 'eMail', 'branche']
        widgets = {
            'firma': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'plz': forms.TextInput(attrs={'class': 'form-control'}),
            'ort': forms.TextInput(attrs={'class': 'form-control'}),
            'eMail': forms.TextInput(attrs={'class': 'form-control'}),
            'branche': forms.Select(attrs={'class': 'form-control'}),
        }

class Anfrage(forms.ModelForm):

    class Meta:
        model = OffertenAnfrage
        fields = ['name', 'plz', 'ort', 'eMail', 'tel', 'beschreibung', 'send']
        labels = {
            'name':'',
            'plz':'',
            'ort':'',
            'eMail':'',
            'tel':'',
            'beschreibung':'',
            'send':'Anfrage an folgende Firmen senden',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name Vorname', 'style': 'margin-top: 20px'}),
            'eMail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail Adresse', 'style': 'margin-top: 20px'}),
            'plz': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postleitzahl', 'style': 'margin-top: 20px'}),
            'ort': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ort', 'style':'margin-top: 20px'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefonummer (optional)', 'style':'margin-top: 20px'}),
            'beschreibung': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:150px; margin-top:20px', 'placeholder': 'Beschreibung...'}),
            'send': forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly', 'style': 'height: 140px'}),
        }
