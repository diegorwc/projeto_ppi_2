# Generated by Django 2.0.13 on 2019-06-19 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions_and_answers', '0003_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquestion',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]