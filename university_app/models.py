from django.db import models
caegoria_docente = {
    ('Instructor','Instructor'),
    ('Docente','Docente'),
    ('Auxiliar','Auxiliar'),
    ('Titular','Titular')
}
grado_cientifico = {
    ('Ninguno','Ninguno'),
    ('Máster','Máster'),
    ('Doctor','Doctor'),
}
agno_academico = {
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
}

class Disciplina (models.Model):
    id_disciplina = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='Nombre')

    def __str__(self):
        return self.nombre

class Profesor (models.Model):
    id_profesor = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    carnet_identidad = models.CharField( max_length=11,verbose_name='Carnet identidad')
    telefono = models.CharField(max_length=10,verbose_name='Teléfono')
    grado_cientifico = models.CharField(max_length=10,verbose_name='Grado científico',choices=grado_cientifico)
    categoria_docente = models.CharField(max_length=10,verbose_name='Categoría docente', choices=caegoria_docente)

    def __str__(self):
        return self.nombre

class Clase (models.Model):
    id_clase = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    agno = models.IntegerField(verbose_name='Año')
    disciplina = models.ForeignKey(Disciplina,blank=True, null=True,on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor,blank=True, null=True,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"
        
    def __str__(self):
        return self.nombre
    
    
    
    
class Estudiante (models.Model):
    id_estudiante = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    carnet_identidad = models.CharField( max_length=11,verbose_name='Carnet identidad')
    telefono = models.CharField(max_length=10,verbose_name='Teléfono')
    direccion = models.CharField(max_length=10,verbose_name='Dirección')
    agno_academico = models.CharField(max_length=10,verbose_name='Año académico', choices=agno_academico)
    fecha = models.DateField(null= True)
    clase = models.ManyToManyField(Clase,blank=True)

    def __str__(self):
        return self.nombre

