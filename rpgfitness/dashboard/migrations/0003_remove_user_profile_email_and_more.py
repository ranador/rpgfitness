# Generated by Django 5.1.3 on 2024-11-17 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_activities_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='password_hash',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='salt',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='user_name',
        ),
    ]
