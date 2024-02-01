from django import forms
from university_app.models import*


class Formulario_clase (forms.Form):
    nombre = forms.CharField(required=True)
    agno = forms.CharField(required=True)
    diciplina = forms.ModelChoiceField(queryset= Disciplina.objects.all())
    profesor = forms.ModelChoiceField(queryset= Profesor.objects.all())