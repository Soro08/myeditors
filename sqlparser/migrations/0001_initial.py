# Generated by Django 2.2.7 on 2019-12-19 17:00

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('minidescription', models.TextField(null=True)),
                ('description', tinymce.models.HTMLField(verbose_name='Content')),
                ('codesql_creation', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Exercices',
                'verbose_name_plural': 'Exercicess',
            },
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Quizz',
                'verbose_name_plural': 'Quizzs',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('enonce', models.TextField()),
                ('codesql_depart', models.TextField()),
                ('codesql_reponse', models.TextField()),
                ('point', models.PositiveIntegerField()),
                ('exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questexo', to='sqlparser.Exercices')),
            ],
            options={
                'verbose_name': 'Questions',
                'verbose_name_plural': 'Questionss',
            },
        ),
        migrations.AddField(
            model_name='exercices',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exoquiz', to='sqlparser.Quizz'),
        ),
    ]
