# Generated by Django 4.2 on 2023-04-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
