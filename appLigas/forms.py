from django import forms
from .models import Deporte, Instalacion, Equipo, Jugador, Partido

class DeporteForm(forms.ModelForm):
    class Meta:
        model = Deporte
        fields = ["nombre"]
        widgets = {            
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
        }

class InstalacionForm(forms.ModelForm):
    class Meta:
        model = Instalacion
        fields = ["nombre", "direccion", "iluminacion", "cubierta"]
        widgets = {            
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "direccion": forms.TextInput(attrs={"class":"form-control"}),
            "iluminacion": forms.CheckboxInput(attrs={"class":"form-check-input"}),
            "cubierta": forms.CheckboxInput(attrs={"class":"form-check-input"}),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ["nombre", "id_deporte", "equipacion_principal", "equipacion_suplente", "contacto", "telefono", "email"]
        exclude = ['id_equipo']
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "id_deporte": forms.Select(attrs={"class":"form-select"}, ),
            "equipacion_principal": forms.TextInput(attrs={"class":"form-control"}),
            "equipacion_suplente": forms.TextInput(attrs={"class":"form-control"}),
            "contacto": forms.TextInput(attrs={"class":"form-control"}),
            "telefono": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
        }

   

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ["nombre", "apellido1", "apellido2", "id_equipo", "dorsal", "fecha_nacimiento", "altura", "peso", "telefono"]
        widgets = {            
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "apellido1": forms.TextInput(attrs={"class":"form-control"}),
            "apellido2": forms.TextInput(attrs={"class":"form-control"}),
            "id_equipo": forms.Select(attrs={"class":"form-select"}),            
            "dorsal": forms.NumberInput(attrs={"class":"form-control"}),
            "fecha_nacimiento": forms.DateInput(attrs={"class":"form-control"}),
            "altura": forms.NumberInput(attrs={"class":"form-control"}),
            "peso": forms.NumberInput(attrs={"class":"form-control"}),
            "telefono": forms.TextInput(attrs={"class":"form-control"}),
        }

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ["id_deporte", "fecha_hora", "id_instalacion", "id_equipo_local", "id_equipo_visitante", "puntos_local", "puntos_visitante", "observaciones"]
        widgets = {            
            "id_deporte": forms.Select(attrs={"class":"form-select"}),
            "fecha_hora": forms.DateTimeInput(attrs={"class":"form-control", "placeholder": "YYYY-MM-DD HH:MM:SS"}),
            "id_instalacion": forms.Select(attrs={"class":"form-select"}),
            "id_equipo_local": forms.Select(attrs={"class":"form-select"}),
            "id_equipo_visitante": forms.Select(attrs={"class":"form-select"}),
            "puntos_local": forms.NumberInput(attrs={"class":"form-control"}),
            "puntos_visitante": forms.NumberInput(attrs={"class":"form-control"}),
            "observaciones": forms.Textarea(attrs={"class":"form-control"}),
        }

    # Método para verificar que el equipo local y visitante sean distintos
    def clean(self):
        cleaned_data = super().clean()
        equipo_local = cleaned_data.get('id_equipo_local')
        equipo_visitante = cleaned_data.get('id_equipo_visitante')

        if equipo_local == equipo_visitante:
            self.add_error(None, forms.ValidationError("El equipo local y el equipo visitante deben ser diferentes.", code='invalid', params={}))
        return cleaned_data
