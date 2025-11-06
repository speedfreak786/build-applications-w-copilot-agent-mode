from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StudentProfile, Activity, Team

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'grade', 'homeroom', 'bio']

class ActivitySerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'student', 'activity_type', 'duration_minutes', 'distance_km', 'date']

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    captain = UserSerializer(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'captain']
