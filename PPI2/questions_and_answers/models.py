from django.db import models
from django.utils import timezone
# Create your models here.

class UserQuestion(models.Model):
    author = models.ForeignKey(
        'auth.User', on_delete = models.CASCADE , null = True,
    )
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(null = True)

    def create_question(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Categoria(models.Model):
    nome = models.CharField(max_length = 100)
    moderador = models.ForeignKey('auth.User', on_delete = models.CASCADE)
