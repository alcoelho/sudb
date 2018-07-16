# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-07 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superuber', '0003_auto_20180707_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='custo',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='departamento',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='fornecedor',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='address',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='gender',
            new_name='genero',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='birthdate',
            new_name='nascimento',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='salary',
            new_name='salario',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='terceirizado',
            new_name='vinculo',
        ),
        migrations.RenameField(
            model_name='projeto',
            old_name='name',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='manager_name',
        ),
        migrations.AddField(
            model_name='custo',
            name='fornecedor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='superuber.Fornecedor'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='cliente',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='superuber.Cliente'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='custo',
            field=models.ManyToManyField(to='superuber.Custo'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='funcionarios',
            field=models.ManyToManyField(to='superuber.Funcionario'),
        ),
    ]