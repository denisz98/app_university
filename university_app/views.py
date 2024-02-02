from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponse
from university_app.models import *
from university_app.form import *
# Create your views here.

# ===========================================CLASE====================================================

def clase(request):
    clases = Clase.objects.all()
    
    return render(request,'clase/Clase.html',{"clases1":clases})


def insertar_clase(request):
    
    miformulario = Formulario_clase()
    claseFormularios = Clase.objects.all()
    
    if request.method == "POST":
        miformulario = Formulario_clase(data = request.POST)
        if miformulario.is_valid():
            
            clase = Clase()
            
            clase.nombre = miformulario.cleaned_data["nombre"]
            clase.agno = miformulario.cleaned_data["agno"]
            clase.disciplina = miformulario.cleaned_data["disciplina"]
            clase.profesor = miformulario.cleaned_data["profesor"]

            clase.save()

            return redirect("Clase")
    
    return render(request,'clase/insertar.html',{"claseFormularios":claseFormularios,"miformulario":miformulario})
def insertar_clase(request):
    
    form=Formulario_clase(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Clase')
    else: print('Error')
    return render(request, 'clase/insertar.html',{'miformulario':form})
    
def editar_clase(request, id_clase):
    clase = Clase.objects.get(id_clase=id_clase)
    formulario = Formulario_clase(instance=clase)
    if request.method == 'POST':
        formulario = Formulario_clase(request.POST, instance=clase)
        if formulario.is_valid():
            formulario.save()
            return redirect('Clase')
    return render(request, 'clase/editar.html', {'miformulario': formulario})

def eliminar_clase(request,id_clase):
    
    clase= Clase.objects.get(pk = id_clase)
    
    clase.delete()
    
    return redirect("Clase")

# ===========================================PROFESOR====================================================



def profesor(request):
    profesor = Profesor.objects.all()
    
    return render(request,'profesor/Profesor.html',{"profesores":profesor})

def insertar_profesor(request):
    
    form=Formulario_profesor(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Profesor')
    else: print('Error')
    return render(request, 'profesor/insertar.html',{'miformulario':form})

def editar_profesor(request, id_profesor):
    profesor = Profesor.objects.get(id_profesor=id_profesor)
    formulario = Formulario_profesor(instance=profesor)
    if request.method == 'POST':
        formulario = Formulario_profesor(request.POST, instance=profesor)
        if formulario.is_valid():
            formulario.save()
            return redirect('Profesor')
    return render(request, 'profesor/editar.html', {'miformulario': formulario})

def eliminar_profesor(request,id_profesor):
    
    profesor= Profesor.objects.get(pk = id_profesor)
    
    profesor.delete()
    
    return redirect("Profesor")
