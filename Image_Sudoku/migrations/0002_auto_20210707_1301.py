# Generated by Django 2.2.5 on 2021-07-07 07:31

import Image_Sudoku.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image_Sudoku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to=Image_Sudoku.models.path_and_rename),
        ),
    ]
