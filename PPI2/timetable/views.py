from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormCurso, FormUnidadeCurricular, FormProfessor, ContatoForm
from .models import Curso, Professor, UnidadeCurricular
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
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

def deleta_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('cursos')

def edita_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = FormCurso(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save()
            return redirect('cursos')
    else:
        # return render(request, 'timetable/edita_curso.html', {'curso': curso})
        form = FormCurso(instance=curso)
    return render(request, 'timetable/edita_curso.html', {'form': form})

def contato(request):
    if request.method == 'GET':
        email_form = ContatoForm()
    else:
        email_form = ContatoForm(request.POST)
        if email_form.is_valid():
            emissor = email_form.cleaned_data['emissor']
            assunto = email_form.cleaned_data['assunto']
            msg = email_form.cleaned_data['msg']

            try:
                send_mail(assunto, msg, emissor, ['wille.diegoricardo@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Erro =/")
            return redirect('obg')
    return render(request, 'timetable/contato.html', {'form': email_form})

def obg(request):
    return HttpResponse("<h2>Obrigado pela mensagem!!!</h2>")

def deleta_curso_confirmacao(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'timetable/excluir_curso.html', {'curso': curso})

# def deleta_professor_confirmacao(request, pk):
    # professor = get_object_or_404(Professor, pk=pk)
    # return HttpResponse("<h2>Else error</h2>")

def deleta_professor_confirmacao(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, 'timetable/excluir_professor.html',
        {'professor': professor})

def deleta_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    professor.delete()
    return redirect('professores')

def professores(request):
    professores = Professor.objects.all()
    lista_cursos = Curso.objects.all()
    lista_unidades_curriculares = UnidadeCurricular.objects.all()

    if request.method == 'POST':
        form = FormProfessor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professores')
        else:
            return HttpResponse("<h2>Else error</h2>")
    else:
        form = FormCurso()
    return render(request, 'timetable/professores.html',
        {'professores': professores, 'form': form, 'lista_cursos': lista_cursos,
        'lista_unidades_curriculares': lista_unidades_curriculares})

def editar_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == "POST":
        form = FormProfessor(request.POST, instance=professor)
        if form.is_valid():
            curso = form.save()
            return redirect('professores')
    else:
        form = FormProfessor(instance=professor)
    return render(request, 'timetable/editar_professor.html', {'form': form})

def editar_uc(request, pk):
    unidade_curricular = get_object_or_404(UnidadeCurricular, pk=pk)
    if request.method == "POST":
        form = FormUnidadeCurricular(request.POST, instance=unidade_curricular)
        if form.is_valid():
            unidade_curricular.dias_das_aulas = ''
            for dia in request.POST.getlist('dias_das_aulas'):
                unidade_curricular.dias_das_aulas += dia
            unidade_curricular = form.save()
            return redirect('unidades_curriculares')
    else:
        form = FormUnidadeCurricular(instance=unidade_curricular)
    # pdb.set_trace()
    return render(request, 'timetable/editar_uc.html', {'form': form,
        'dias_das_aulas': unidade_curricular.dias_das_aulas})

def deleta_uc_confirmacao(request, pk):
    unidade_curricular = get_object_or_404(UnidadeCurricular, pk=pk)
    return render(request, 'timetable/excluir_unidade_curricular.html',
        {'unidade_curricular': unidade_curricular})

def deleta_uc(request, pk):
    unidade_curricular = get_object_or_404(UnidadeCurricular, pk=pk)
    unidade_curricular.delete()
    return redirect('unidades_curriculares')

class registrar_usuario(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts/login')
    template_name = 'registration/registrar_usuario.html'

def valida_usuario(request):
    usuario = request.GET.get('usuario', None)    
    dados = {
        'usuario': usuario,
        'em_uso': User.objects.filter(username=usuario).exists()
    }
    return JsonResponse(dados)
