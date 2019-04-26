from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('cursos/', views.cursos, name='cursos'),
    path(
        'unidades_curriculares', views.unidades_curriculares,
        name='unidades_curriculares'
    ),
]
