from django.urls import path, include
from university_app import views

urlpatterns = [
    path('clase/', views.clase, name="Clase"),

]