from django.shortcuts import render, redirect
from .forms import FormCurso, FormUnidadeCurricular
from .models import Curso, Professor, UnidadeCurricular
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import pdb

# Create your views here.
def home(request):
    return render(request, 'timetable/home.html')

@login_required
def cursos(request):
    lista_cursos = Curso.objects.all()
    uc_por_curso = {}
    for curso in lista_cursos:
        uc_por_curso[curso.nome] = UnidadeCurricular.objects.filter(
            curso_id = Curso.objects.get(nome = curso.nome).id
        )

    if request.method == 'POST':
        form = FormCurso(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
        else:
            return redirect('home')
    else:
        form = FormCurso()
        # pdb.set_trace()
    string_dias = ""
    for num in range(2, 7):
        string_dias += str(num)
    return render(
        request, 'timetable/cursos.html', {'form': form,
        'lista_cursos': lista_cursos, 'uc_por_curso': uc_por_curso,
        'range': string_dias}
    )

@login_required
def unidades_curriculares(request):
    lista_unidades_curriculares = UnidadeCurricular.objects.all()

    if request.method == 'POST':
        form = FormUnidadeCurricular(request.POST)
        if form.is_valid():
            nova_uc = form.save(commit=False)
            nova_uc.dias_das_aulas = ''
            for dia in request.POST.getlist('dias_das_aulas'):
                nova_uc.dias_das_aulas += dia
            nova_uc.horario_de_inicio = str(nova_uc.horario_de_inicio)
            nova_uc.horario_de_termino = str(nova_uc.horario_de_termino)
            nova_uc.save()
            # pdb.set_trace()
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
