# Generated by Django 3.1.4 on 2021-01-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210122_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='two',
            name='board',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
