# Generated by Django 4.1.1 on 2022-11-16 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_tipo_perfil_inicio_estadisticas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_perfil',
            name='autorizar_req',
        ),
        migrations.RemoveField(
            model_name='tipo_perfil',
            name='autorizar_sol',
        ),
        migrations.RemoveField(
            model_name='tipo_perfil',
            name='crear_sol',
        ),
        migrations.RemoveField(
            model_name='tipo_perfil',
            name='ver_req',
        ),
        migrations.RemoveField(
            model_name='tipo_perfil',
            name='ver_sol',
        ),
    ]
