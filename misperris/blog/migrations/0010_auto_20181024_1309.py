# Generated by Django 2.1.2 on 2018-10-24 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181024_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='perro/%Y'),
        ),
    ]