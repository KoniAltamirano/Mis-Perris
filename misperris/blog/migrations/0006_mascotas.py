# Generated by Django 2.1.2 on 2018-10-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181024_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.FileField(blank=True, null=True, upload_to='perro/%Y/%m/%D')),
                ('nombre', models.CharField(max_length=30)),
                ('raza', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
            ],
        ),
    ]
