# Generated by Django 3.1.4 on 2021-01-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_one_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='one',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
