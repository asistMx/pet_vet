# Generated by Django 5.0.4 on 2024-04-18 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
       
        ('authentication', '0002_user_created_user_empresa_user_sucursal_user_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.empleado'),
        ),
    ]
