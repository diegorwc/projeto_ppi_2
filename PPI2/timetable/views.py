from django.shortcuts import render, redirect
from .forms import FormCurso, FormUnidadeCurricular
from .models import Curso, Professor, UnidadeCurricular
from django.http import HttpResponseRedirect
import pdb, logging

logger = logging.getLogger(__name__)

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
    lista_unidades_curriculares = UnidadeCurricular.objects.all()
    if request.method == 'POST':
        form = FormUnidadeCurricular(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unidades_curriculares')
        else:
             pdb.set_trace()
            # return redirect('FORM_NOT_VALID')
    else:
        form = FormUnidadeCurricular()
        # pdb.set_trace()        
    return render(
        request, 'timetable/unidades_curriculares.html', {'form': form,
        'lista_unidades_curriculares': lista_unidades_curriculares}
    )
