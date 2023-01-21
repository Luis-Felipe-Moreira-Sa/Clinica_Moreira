# Generated by Django 4.0.1 on 2023-01-18 19:43

from django.db import migrations, models
import medicos.models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_alter_medico_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='dia',
            field=models.DateField(help_text='Anexe uma data para a agenda', validators=[medicos.models.validar_dia]),
        ),
    ]
