from django.shortcuts import render, redirect
from .forms import FormCurso
from .models import Curso, Professor
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'timetable/home.html')

def cursos(request):
    lista_cursos = Curso.objects.all()
    if request.method == 'POST':
        form = FormCurso(request.POST)
        form.coordenador = Professor.objects.get(nome='Diego')
        if form.is_valid():
            form.save(commit=False)
            form.coordenador = Professor.objects.get(nome='Diego')
            form.save()
            return redirect('cursos')
        else:
            return redirect('home')
    else:
        form = FormCurso()
    return render(
        request, 'timetable/cursos.html', {'form': form,
        'lista_cursos': lista_cursos}
    )
