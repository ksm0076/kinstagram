# Generated by Django 5.1 on 2024-09-03 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_remove_feed_like_count_remove_feed_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='user_id',
            new_name='user_email',
        ),
    ]
