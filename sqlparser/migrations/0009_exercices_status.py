# Generated by Django 2.2.7 on 2019-12-18 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlparser', '0008_exercices_minidescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercices',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]