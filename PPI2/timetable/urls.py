from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/', views.cursos, name='cursos'),
    path(
        'unidades_curriculares', views.unidades_curriculares,
        name='unidades_curriculares'
    ),
    path('horarios/', include('django.contrib.auth.urls')),
    path('cursos/<pk>/deleta_curso', views.deleta_curso, name='deleta_curso'),
]
