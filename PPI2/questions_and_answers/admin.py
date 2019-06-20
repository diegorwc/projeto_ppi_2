from django.contrib import admin
from .models import UserQuestion, Resposta, Categoria

# Register your models here.
admin.site.register(UserQuestion)
admin.site.register(Categoria)
admin.site.register(Resposta)
