# Generated by Django 3.2.5 on 2022-09-06 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20220902_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulosparasurtir',
            old_name='firma',
            new_name='selecionado',
        ),
        migrations.RenameField(
            model_name='historicalarticulosparasurtir',
            old_name='firma',
            new_name='selecionado',
        ),
    ]
