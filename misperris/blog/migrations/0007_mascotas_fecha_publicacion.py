# Generated by Django 2.1.2 on 2018-10-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_mascotas'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascotas',
            name='fecha_publicacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
