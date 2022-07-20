# Generated by Django 4.0.5 on 2022-07-20 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Academia_Arte', '0016_alter_estudiante_curso_estudiante'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
