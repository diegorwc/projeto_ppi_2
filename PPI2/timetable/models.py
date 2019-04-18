from django.db import models

#https://docs.djangoproject.com/en/2.2/ref/models/fields/#model-field-types

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_de_modulos = models.IntegerField()
    coordenador = models.ForeignKey('Professor', on_delete=models.SET_NULL,
    null=True)

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    sala = models.CharField(max_length=50)
    modulo_atual = models.IntegerField()
    horario_de_inicio = models.TimeField()
    horario_de_termino = models.TimeField()
    fk_professor = models.ForeignKey('Professor', on_delete=models.SET_NULL,
    null=True)
    fk_curso = models.ForeignKey('Curso', on_delete=models.SET_NULL,
    null=True)

class Professor(models.Model):
    Professor = models.CharField(max_length=50)
