# Generated by Django 4.2b1 on 2023-04-09 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppKaren', '0003_visita_delete_destino_rename_nombre_paquete_lugar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paquete',
        ),
        migrations.DeleteModel(
            name='Viajero',
        ),
        migrations.DeleteModel(
            name='Visita',
        ),
    ]
