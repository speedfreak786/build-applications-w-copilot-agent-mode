from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    grade = models.PositiveSmallIntegerField(null=True, blank=True)
    homeroom = models.CharField(max_length=64, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} (Grade {self.grade})"

class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('run', 'Run'),
        ('walk', 'Walk'),
        ('bike', 'Bike'),
        ('swim', 'Swim'),
        ('game', 'Team Game'),
        ('other', 'Other'),
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.student.username} {self.activity_type} {self.date}"

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    captain = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='captain_of')

    def __str__(self):
        return self.name
