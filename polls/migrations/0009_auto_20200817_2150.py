# Generated by Django 3.1 on 2020-08-17 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_questionnaire_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Начало теста'),
        ),
        migrations.RemoveField(
            model_name='questioninquestionnaire',
            name='question',
        ),
        migrations.AddField(
            model_name='questioninquestionnaire',
            name='question',
            field=models.ManyToManyField(null=True, related_name='question', to='polls.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Начало теста'),
        ),
    ]