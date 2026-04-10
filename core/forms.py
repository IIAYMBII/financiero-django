from django import forms
from .models import Ingreso, Gasto

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['descripcion', 'monto', 'fecha']


class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion', 'monto', 'tipo', 'fecha', 'categoria']