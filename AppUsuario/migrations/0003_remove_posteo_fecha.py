# Generated by Django 4.1.3 on 2022-11-15 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuario', '0002_postcriticas_posteo_postnoticias_delete_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='fecha',
        ),
    ]
