# Generated by Django 4.1.2 on 2022-11-24 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_precio_productos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='precio',
        ),
    ]