# Generated by Django 2.1.2 on 2018-10-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20181019_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='desc_for_find',
            field=models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска'),
        ),
        migrations.AddField(
            model_name='articles',
            name='keywords',
            field=models.CharField(blank=True, max_length=200, verbose_name='Кейвордс'),
        ),
    ]