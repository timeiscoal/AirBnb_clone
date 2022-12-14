# Generated by Django 4.1.3 on 2022-11-20 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0003_alter_experience_category_alter_experience_perk'),
        ('medias', '0002_alter_photo_file_alter_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='experience',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='experiences.experience'),
        ),
    ]
