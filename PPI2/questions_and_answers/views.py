from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import UserQuestion
from .forms import UserQuestionForm, UserQuestionAnswer
from django.http import HttpResponseRedirect
import pdb

def home(request):
    if request.method == 'POST':
        form = UserQuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.author = request.user
            new_question.save()
            return redirect('questions_list')
    else:
        form = UserQuestionForm()
    return render(request, 'questions_and_answers/base.html', {'form': form})

def questions_list(request):
    # users_questions = UserQuestion.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    users_questions = UserQuestion.objects.all()
    # return render(request, 'questions_and_answers/questions_cards.html', {'users_questions': users_questions})
    if request.method == 'POST':
        form = UserQuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            # pdb.set_trace()
            if request.user.is_anonymous:
                request.user = None
            else:
                new_question.author = request.user
            new_question.save()
            return redirect('questions_list')
    else:
        form = UserQuestionForm()
    return render(request, 'questions_and_answers/questions_cards.html',
    {'form': form, 'users_questions': users_questions})

def detalhes_pergunta(request, pk):
    user_question = get_object_or_404(UserQuestion, pk=pk)
    return render(
        request, 'questions_and_answers/detalhes_pergunta.html',
        {'user_question': user_question}
    )

def add_answer_to_question(request, pk):
    user_question = get_object_or_404(UserQuestion, pk=pk)
    if request.method == 'POST':
        form = UserQuestionAnswer(request.POST)
        if form.is_valid():
            resposta = form.save(commit = False)
            resposta.user_question = user_question
            resposta.save()
            return redirect('detalhes_pergunta', pk = user_question.pk)
    else:
        form = UserQuestionAnswer()
    return render(
        request, 'questions_and_answers/add_answer_to_question.html',
        {'form': form}
    )

def deleta_questao(request, pk):
    user_question = get_object_or_404(UserQuestion, pk=pk)
    user_question.delete()
    return redirect('questions_list')
