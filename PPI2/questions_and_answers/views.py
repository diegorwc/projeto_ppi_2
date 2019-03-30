from django.shortcuts import render

def home(request):
    return render(request, 'questions_and_answers/home.html', {})
