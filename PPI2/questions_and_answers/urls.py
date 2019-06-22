from django.urls import path
from . import views

urlpatterns = [
    # path('', views.questions_list, name='home'),
    path('', views.questions_list, name = 'questions_list'),
    # path('', views.questions_list, name='questions_list'),
    path('teste', views.teste, name = 'teste'),
    path('pergunta/<pk>/', views.detalhes_pergunta,
        name = 'detalhes_pergunta'),
    path(
        'pergunta/<pk>/resposta/', views.add_answer_to_question,
        name = 'add_answer_to_question'
    ),
    path(
        'pergunta/<pk>/deletar', views.deleta_questao, name = 'deleta_questao'
    ),

]
