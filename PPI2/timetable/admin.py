from django.contrib import admin
from .models import Curso, Professor, UnidadeCurricular

# Register your models here.
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(UnidadeCurricular)
