from django.contrib import admin
from university_app.models import *



class Estudiante_admin(admin.ModelAdmin):
    list_display = ("nombre", "carnet_identidad", "telefono","fecha")
    search_fields = ("nombre","telefono")
    list_filter = ("nombre","fecha")

class Clase_admin(admin.ModelAdmin):
    list_display = ("nombre", "agno")
    search_fields = ("nombre",)
    list_filter = ("nombre",)

class Profesor_admin(admin.ModelAdmin):
    list_display = ("nombre", "carnet_identidad", "telefono")
    search_fields = ("nombre","telefono","grado_cientifico" )

admin.site.register(Disciplina)
admin.site.register(Estudiante, Estudiante_admin)
admin.site.register(Profesor, Profesor_admin)
admin.site.register(Clase, Clase_admin)