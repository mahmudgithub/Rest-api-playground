# Generated by Django 3.1.4 on 2021-01-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='two',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='two',
            name='roll',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
