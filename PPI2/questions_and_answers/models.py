from django.db import models
from django.utils import timezone
# Create your models here.

class UserQuestion(models.Model):
    author = models.ForeignKey(
        'auth.User', on_delete = models.CASCADE , null = True,
    )
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def create_question(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Categoria(models.Model):
    nome = models.CharField(max_length = 100)
    moderador = models.ForeignKey('auth.User', on_delete = models.CASCADE)

class Resposta(models.Model):
    user_question = models.ForeignKey(
        'questions_and_answers.UserQuestion', on_delete = models.CASCADE,
        related_name = 'respostas'
    )
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text
