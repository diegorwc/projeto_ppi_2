from django.urls import path
from . import views

urlpatterns = [
    # path('', views.questions_list, name='home'),
    path('', views.questions_list, name='questions_list'),
    # path('', views.questions_list, name='questions_list'),
    path('teste', views.teste, name='teste')
]
