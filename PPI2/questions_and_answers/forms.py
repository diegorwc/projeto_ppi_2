from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import UserQuestion
from django.utils.translation import gettext_lazy as _

#https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/#specifying-widgets-to-use-in-the-form-with-widgets
#https://docs.djangoproject.com/en/dev/ref/forms/widgets/#django.forms.Widget.attrs

class UserQuestionForm(forms.ModelForm):

    class Meta:
        model = UserQuestion
        fields = ('title', 'text')

        widgets = {
            'title': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'text': Textarea(attrs={'class': 'mdl-textfield__input'})
        }
