# Generated by Django 2.2.7 on 2019-12-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlparser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercices',
            name='codesql_depart',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]