from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questions', views.questions_list, name='questions_list'),
    path('perguntas', views.questions_list, name='questions_list'),
]
