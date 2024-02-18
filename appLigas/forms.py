from django import forms
from django.db import models

class DeportesForm(forms.ModelForm):
    class Meta:
        model = models.Model
        fields = ["id_deporte", "nombre"]
        widgets = {
            "id_deporte": forms.TextInput(attrs={"class":"form-control"}),
            "nombre": forms.TextInput(attrs={"class":"form-control"}),            
        }