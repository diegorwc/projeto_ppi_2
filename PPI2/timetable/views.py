from django.shortcuts import render, redirect
from .forms import FormCurso
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'timetable/home.html')

def cursos(request):
    if request.method == 'POST':
        form = FormCurso(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = FormCurso()
    return render(request, 'timetable/cursos.html', {'form': form})    
