from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponse
from university_app.models import *
# from university_app.form import *
# Create your views here.



def clase(request):
    clases = Clase.objects.all()
    
    return render(request,'clase/Clase.html',{"clases1":clases})

