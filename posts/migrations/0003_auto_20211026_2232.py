# Generated by Django 3.1.13 on 2021-10-26 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211013_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.CharField(max_length=1000),
        ),
    ]