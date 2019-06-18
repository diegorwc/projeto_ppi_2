from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.generic import TemplateView
from questions_and_answers import urls


urlpatterns = [
    path('', views.cursos, name='home'),
    path('cursos/', views.cursos, name='cursos'),
    path(
        'unidades_curriculares', views.unidades_curriculares,
        name='unidades_curriculares'
    ),
    path('horarios/', include('django.contrib.auth.urls')),
    path('perguntas/', include('questions_and_answers.urls')),
    path('cursos/<pk>/deleta_curso', views.deleta_curso, name='deleta_curso'),
    path('cursos/<pk>/deleta_curso_confirmacao', views.deleta_curso_confirmacao,
        name='deleta_curso_confirmacao'),
    path('cursos/<pk>/edita_curso', views.edita_curso, name='edita_curso'),
    path('contato/', views.contato, name='contato'),
    path('contato/obg', views.obg, name='obg'),
    path('professores', views.professores, name='professores'),
    path('professores/<pk>/deleta_professor_confirmacao',
        views.deleta_professor_confirmacao,name='deleta_professor_confirmacao'),
    path('professores/<pk>/deleta_professor', views.deleta_professor,
        name='deleta_professor'),
    path('professores/<pk>/edita_professor', views.editar_professor,
        name='editar_professor'),
    path('unidades_curriculares/<pk>/deleta_unidade_curricular_confirmacao',
        views.deleta_uc_confirmacao, name='deleta_uc_confirmacao'),
    path('unidades_curriculares/<pk>/deleta_unidade_curricular',
        views.deleta_uc, name='deleta_uc'),
    path('unidades_curriculares/<pk>/edita_unidade_curricular',
        views.editar_uc, name='editar_unidade_curricular'),
    path('registrar_usuario/', views.registrar_usuario.as_view(),
        name="registrar_usuario"),
    path('valida_usuario/', views.valida_usuario, name="valida_usuario"),
    path('reseta_senha/', views.password, name="reseta_senha"),
]
