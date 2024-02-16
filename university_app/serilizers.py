from rest_framework import serializers
from.models import*
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = "__all__"
class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = "__all__"