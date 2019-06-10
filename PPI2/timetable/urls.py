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
    path('cursos/<pk>/deleta_curso_confirmacao', views.deleta_curso_confirmacao,
        name='deleta_curso_confirmacao'),
    path('cursos/<pk>/edita_curso', views.edita_curso, name='edita_curso'),
    path('contato/', views.contato, name='contato'),
    path('contato/obg', views.obg, name='obg'),
]
