# Generated by Django 2.0.13 on 2019-04-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20190419_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='turno',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno'), ('Integral', 'Integral')], default='Matutino', max_length=10),
        ),
    ]
