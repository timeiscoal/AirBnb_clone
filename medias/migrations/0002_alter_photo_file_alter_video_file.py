# Generated by Django 4.1.3 on 2022-11-20 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
