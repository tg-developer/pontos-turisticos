# Generated by Django 2.2.4 on 2019-08-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0002_pontosturisticos_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]
