# Generated by Django 5.0.4 on 2024-04-27 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='imagen2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='imagen3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='microchip',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]