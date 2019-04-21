from django.shortcuts import render, redirect
from .forms import FormCurso, FormUnidadeCurricular
from .models import Curso, Professor
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'timetable/home.html')

def cursos(request):
    lista_cursos = Curso.objects.all()
    if request.method == 'POST':
        form = FormCurso(request.POST)
        if form.is_valid():
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

def unidades_curriculares(request):
    if request.method == 'POST':
        form = FormUnidadeCurricular(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unidades_curriculares')
        else:
            return redirect('FORM_NOT_VALID')
    else:
        form = FormUnidadeCurricular()
    return render(
        request, 'timetable/unidades_curriculares.html', {'form': form}
    )
