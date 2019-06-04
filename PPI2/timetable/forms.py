from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput, Select, \
TimeInput, CheckboxInput, SelectMultiple
from .models import Curso, UnidadeCurricular
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

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
            #     attrs={'id': 'id_dias_das_aulas'}
            # ),
            'professor': Select(attrs={'class': 'mdl-textfield__input'}),
            'curso': Select(attrs={'class': 'mdl-textfield__input'}),
        }

class ContatoForm(forms.Form):
    emissor = forms.EmailField(required=True, label='Remetente')
    assunto = forms.CharField(required=True)
    msg = forms.CharField(widget=forms.Textarea, label='Mensagem')


    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('emissor', css_class='form-group col-md-6'),
                Column('assunto', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'msg'
        )
        self.helper.add_input(Submit('submit', 'Enviar'))
        # self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))
