# Generated by Django 2.1.2 on 2018-10-24 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181024_0159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'permissions': (('usuario', 'Usuario'),)},
        ),
    ]
