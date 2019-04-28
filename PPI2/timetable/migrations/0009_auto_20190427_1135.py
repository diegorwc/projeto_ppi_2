# Generated by Django 2.0.13 on 2019-04-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_unidadecurricular_dias_das_aulas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadecurricular',
            name='dias_das_aulas',
            field=models.CharField(choices=[('2', 'Segunda-feira'), ('3', 'Terça-feira'), ('4', 'Quarta-feira'), ('5', 'Quinta-feira'), ('6', 'Sexta-feira')], default='Segunda-feira', max_length=3),
        ),
    ]