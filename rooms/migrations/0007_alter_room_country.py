# Generated by Django 4.1.3 on 2022-11-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_alter_room_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='country',
            field=models.CharField(choices=[('default', '나라 선택하기'), ('ko', '한국'), ('usa', '미국'), ('japan', '일본')], default='default', max_length=100),
        ),
    ]
