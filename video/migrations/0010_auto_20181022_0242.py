# Generated by Django 2.1.2 on 2018-10-21 23:42

from django.db import migrations, models
import video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0009_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='img_file',
            field=models.ImageField(blank=True, null=True, upload_to=video.models.generate_filename_jpg, verbose_name='IMG'),
        ),
        migrations.AddField(
            model_name='video',
            name='img_file',
            field=models.ImageField(blank=True, null=True, upload_to=video.models.generate_filename_jpg, verbose_name='IMG'),
        ),
    ]
