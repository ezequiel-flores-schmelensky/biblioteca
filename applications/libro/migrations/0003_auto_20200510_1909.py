# Generated by Django 3.0.6 on 2020-05-11 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_auto_20200508_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo', 'fecha'], 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
    ]
