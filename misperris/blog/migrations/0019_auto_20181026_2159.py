# Generated by Django 2.1.2 on 2018-10-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20181026_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre_user',
            field=models.CharField(max_length=30),
        ),
    ]
