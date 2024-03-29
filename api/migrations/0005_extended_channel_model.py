# Generated by Django 4.0.1 on 2022-01-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_added_youtube_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='channel_id',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='channel_logo',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='channel_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
