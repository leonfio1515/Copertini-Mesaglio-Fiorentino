# Generated by Django 4.0.3 on 2022-07-21 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academia_Arte', '0017_estudiante_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='curso_estudiante',
            field=models.CharField(max_length=50),
        ),
    ]
