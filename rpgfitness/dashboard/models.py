from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    strava_id = models.IntegerField()
    name = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.DateTimeField() 
    duration_seconds = models.IntegerField()
    avg_power_watts = models.FloatField()
    avg_speed_mps = models.FloatField()
    elevation_gain_m = models.FloatField()
    start_lat = models.FloatField()
    start_lng = models.FloatField()
    end_lat = models.FloatField()
    end_lng = models.FloatField()
    gps_data = models.JSONField()
    calories = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self

class User_profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    date_of_birth = models.DateField(blank=True, null=True)
    strava_athlete_id = models.IntegerField(blank=True, null=True)
    strava_refresh_token = models.CharField(max_length=255, blank=True, null=True)
    strava_access_token = models.CharField(max_length=255, blank=True, null=True)
    strava_token_expires_at = models.DateTimeField(blank=True, null=True)
    strava_connected_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    current_xp = models.IntegerField()
    current_level = models.IntegerField()
    distance_biked_km = models.FloatField(blank=True, null=True)
    distance_run_km = models.FloatField(blank=True, null=True)
    distance_swam_km = models.FloatField(blank=True, null=True)
    distance_walked_km = models.FloatField(blank=True, null=True)
    distance_hiked_km = models.FloatField(blank=True, null=True)
    
    createxd_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User: {self.user_id} ({self.strava_athlete_id}), level {self.current_level} with {self.current_xp} XP'