# Generated by Django 2.0.13 on 2019-04-21 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_auto_20190421_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unidadecurricular',
            old_name='fk_curso',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='unidadecurricular',
            old_name='modulo_atual',
            new_name='modulo',
        ),
        migrations.RenameField(
            model_name='unidadecurricular',
            old_name='fk_professor',
            new_name='professor',
        ),
    ]
