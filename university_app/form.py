from django import forms
from university_app.models import*
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


# class Formulario_clase (forms.Form):
#     nombre = forms.CharField(required=True)
#     agno = forms.CharField(required=True)
#     disciplina = forms.ModelChoiceField(queryset= Disciplina.objects.all())
#     profesor = forms.ModelChoiceField(queryset= Profesor.objects.all())

class Formulario_clase(forms.ModelForm):
    class Meta:
        model=Clase
        fields='__all__'
        
class Formulario_profesor(forms.ModelForm):
    class Meta:
        model=Profesor
        fields='__all__'
