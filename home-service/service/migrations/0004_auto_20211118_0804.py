# Generated by Django 3.1 on 2021-11-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20211118_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(),
        ),
    ]