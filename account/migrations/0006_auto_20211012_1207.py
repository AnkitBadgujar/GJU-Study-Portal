# Generated by Django 3.1.5 on 2021-10-12 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20211012_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due',
            field=models.DateTimeField(auto_now=True),
        ),
    ]