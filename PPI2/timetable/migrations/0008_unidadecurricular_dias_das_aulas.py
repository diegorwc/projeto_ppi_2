# Generated by Django 2.0.13 on 2019-04-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0007_auto_20190421_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidadecurricular',
            name='dias_das_aulas',
            field=models.CharField(choices=[('segunda-feira', 'Segunda-feira'), ('terça-feira', 'Terça-feira'), ('quarta-feira', 'Quarta-feira'), ('quinta-feira', 'Quinta-feira'), ('sexta-feira', 'Sexta-feira')], default='Segunda-feira', max_length=20),
        ),
    ]
