# Generated by Django 3.0.6 on 2020-05-17 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_content_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='likes',
            new_name='like',
        ),
    ]
