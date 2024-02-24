from django.urls import path, include
from rest_framework import routers
from .viewsets import *


router = routers.DefaultRouter()
router.register(r'estudiante2', EstudianteViewsets)
router.register(r'clase', ClaseViewsets)


urlpatterns = router.urls

    
