# Generated by Django 3.2.20 on 2023-09-09 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='rating',
        ),
    ]
