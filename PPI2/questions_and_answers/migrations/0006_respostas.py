# Generated by Django 2.0.13 on 2019-06-20 17:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions_and_answers', '0005_auto_20190620_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respostas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='questions_and_answers.UserQuestion')),
            ],
        ),
    ]
