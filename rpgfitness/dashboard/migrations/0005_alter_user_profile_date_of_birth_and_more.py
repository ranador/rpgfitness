# Generated by Django 5.1.3 on 2024-11-18 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_user_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='distance_biked_km',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='distance_hiked_km',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='distance_run_km',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='distance_swam_km',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='distance_walked_km',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='strava_access_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='strava_athlete_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='strava_connected_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='strava_refresh_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='strava_token_expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
