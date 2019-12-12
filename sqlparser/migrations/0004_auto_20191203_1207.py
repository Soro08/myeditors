# Generated by Django 2.2.7 on 2019-12-03 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqlparser', '0003_auto_20191203_1042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tests',
            options={'verbose_name': 'Tests', 'verbose_name_plural': 'Tests'},
        ),
        migrations.AddField(
            model_name='tests',
            name='exercice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='testexo', to='sqlparser.Exercices'),
        ),
    ]