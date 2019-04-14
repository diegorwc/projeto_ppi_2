from django.shortcuts import render, redirect
from django.utils import timezone
from .models import UserQuestion
from .forms import UserQuestionForm
from django.http import HttpResponseRedirect

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
            new_question.author = request.user
            new_question.save()
            return redirect('questions_list')
    else:
        form = UserQuestionForm()
    return render(request, 'questions_and_answers/questions_cards.html',
    {'form': form, 'users_questions': users_questions})
