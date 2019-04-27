from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput, Select, \
TimeInput, CheckboxInput, SelectMultiple
from .models import Curso, UnidadeCurricular
class FormCurso(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ('nome', 'quantidade_de_modulos', 'coordenador', 'turno')

        widgets = {
            'nome': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'coordenador': Select(attrs={'class': 'mdl-textfield__input'}),
            'quantidade_de_modulos':  TextInput(attrs={'class': 'mdl-textfield__input',
            'pattern': '-?[0-9]*(\.[0-9]+)?'}),
            'turno': Select(attrs={'class': 'mdl-textfield__input'}),
        }

class FormUnidadeCurricular(forms.ModelForm):

    class Meta:
        model = UnidadeCurricular

        fields = (
            'nome', 'carga_horaria', 'sala', 'modulo', 'horario_de_inicio',
            'horario_de_termino', 'professor', 'curso', 'dias_das_aulas',
        )

        widgets = {
            'nome': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'carga_horaria': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'sala': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'modulo': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'horario_de_inicio': TimeInput(attrs={'class': 'mdl-textfield__input',
            'type': 'time'}),
            'horario_de_termino': TimeInput(attrs={'class': 'mdl-textfield__input',
            'type': 'time'}),
            # 'dias_das_aulas': Select(
            #     attrs={'class': 'mdl-textfield__input'}
            # ),
            'professor': Select(attrs={'class': 'mdl-textfield__input'}),
            'curso': Select(attrs={'class': 'mdl-textfield__input'}),
        }
