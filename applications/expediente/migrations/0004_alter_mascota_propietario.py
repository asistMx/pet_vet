# Generated by Django 5.0.4 on 2024-04-27 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0003_propietario_apellido_materno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mascotas', to='expediente.propietario'),
        ),
    ]
