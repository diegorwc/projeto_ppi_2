from django.db import models

#https://docs.djangoproject.com/en/2.2/ref/models/fields/#model-field-types

class Professor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Curso(models.Model):

    MATUTINO = 'Matutino'
    VESPERTINO = 'Vespertino'
    NOTURNO = 'Noturno'
    INTEGRAL = 'Integral'
    OPCOES_TURNO = (
        (MATUTINO, 'Matutino'),
        (VESPERTINO, 'Vespertino'),
        (NOTURNO, 'Noturno'),
        (INTEGRAL, 'Integral'),
    )

    # PROFESSORES = Professor.objects.all()

    nome = models.CharField(max_length=100)
    quantidade_de_modulos = models.IntegerField()
    coordenador = models.ForeignKey(
        'Professor', on_delete=models.SET_NULL, null=True
    )
    # coordenador = models.CharField(max_length = 100, null=True)
    turno = models.CharField(
        max_length = 10, choices=OPCOES_TURNO, default='Matutino',
    )

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    sala = models.CharField(max_length=50)
    modulo = models.IntegerField()
    horario_de_inicio = models.TimeField()
    horario_de_termino = models.TimeField()
    professor = models.ForeignKey('Professor', on_delete=models.SET_NULL,
    null=True)
    curso = models.ForeignKey('Curso', on_delete=models.SET_NULL,
    null=True)

    def __str__(self):
        return self.nome
