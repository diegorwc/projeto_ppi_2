from django.db import models

#https://docs.djangoproject.com/en/2.2/ref/models/fields/#model-field-types

class Course(models.Model):
    name = models.CharField(max_length=100)
    modules_amount = models.IntegerField()
    coordinator = models.ForeignKey('Teacher', on_delete=models.SET_NULL,
    null=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    workload = models.IntegerField()
    classroom = models.CharField(max_length=50)
    current_module = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    fk_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL,
    null=True)
    fk_course = models.ForeignKey('Course', on_delete=models.SET_NULL,
    null=True)

class Teacher(models.Model):
    teacher = models.CharField(max_length=50)
