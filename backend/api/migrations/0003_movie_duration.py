# Generated by Django 5.1.2 on 2024-11-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_channel_banner_channel_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
