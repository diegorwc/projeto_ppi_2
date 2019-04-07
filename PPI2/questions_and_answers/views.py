from django.shortcuts import render
from django.utils import timezone
from .models import UserQuestion

def home(request):
    return render(request, 'questions_and_answers/base.html', {})

def questions_list(request):
    users_questions = UserQuestion.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'questions_and_answers/questions_cards.html', {'users_questions': users_questions})
