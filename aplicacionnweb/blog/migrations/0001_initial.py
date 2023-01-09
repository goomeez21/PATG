# Generated by Django 4.1.2 on 2022-11-19 23:35

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.IntegerField()),
                ('barrio', models.CharField(max_length=250)),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=25830)),
            ],
        ),
    ]