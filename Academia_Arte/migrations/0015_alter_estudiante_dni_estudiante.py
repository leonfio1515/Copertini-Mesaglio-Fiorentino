# Generated by Django 4.0.3 on 2022-07-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academia_Arte', '0014_estudiante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='dni_estudiante',
            field=models.CharField(max_length=12),
        ),
    ]