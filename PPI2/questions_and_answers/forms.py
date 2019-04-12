from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import UserQuestion
from django.utils.translation import gettext_lazy as _

class UserQuestionForm(forms.ModelForm):

    class Meta:
        model = UserQuestion
        fields = ('title', 'text')

        widgets = {
            'title': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'text': Textarea(attrs={'class': 'mdl-textfield__input'})
        }

        # labels = {
        #     'title': _(''),
        # }
