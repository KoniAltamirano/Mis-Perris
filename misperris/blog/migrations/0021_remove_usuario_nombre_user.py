# Generated by Django 2.1.2 on 2018-10-27 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20181026_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nombre_user',
        ),
    ]
