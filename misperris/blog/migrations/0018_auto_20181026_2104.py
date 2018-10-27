# Generated by Django 2.1.2 on 2018-10-27 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20181025_0545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mascotas',
            options={'permissions': (('mantenedor_mascotas', 'Mascotas'),)},
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
