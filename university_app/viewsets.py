from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponse
from university_app.models import *
from university_app.serilizers import *
from rest_framework import viewsets
# from university_app.form import *
# Create your views here.


class EstudianteViewsets(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
class ClaseViewsets(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer