from django.contrib import admin
from university_app.models import *



class Estudiante_admin(admin.ModelAdmin):
    list_display = ("nombre", "carnet_identidad", "telefono","fecha")
    search_fields = ("nombre","telefono")
    list_filter = ("nombre","fecha")


admin.site.register(Disciplina)
admin.site.register(Estudiante, Estudiante_admin)
admin.site.register(Profesor)
admin.site.register(Clase)