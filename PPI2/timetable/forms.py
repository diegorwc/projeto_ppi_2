from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput, Select
from .models import Curso

class FormCurso(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ('nome', 'quantidade_de_modulos', 'coordenador', 'turno')

        widgets = {
            'nome': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'coordenador': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'quantidade_de_modulos':  TextInput(attrs={'class': 'mdl-textfield__input',
            'pattern': '-?[0-9]*(\.[0-9]+)?'}),
            'turno': Select(attrs={}),
        }
