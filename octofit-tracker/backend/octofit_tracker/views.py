from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import StudentProfile, Activity, Team
from .serializers import UserSerializer, StudentProfileSerializer, ActivitySerializer, TeamSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.select_related('user').all()
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.select_related('student').all().order_by('-date')
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # teacher can create on behalf of a student by specifying student in payload in real app
        serializer.save()

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related('members').all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def leaderboard(self, request):
        # simple leaderboard: sum of activity duration per user
        qs = Activity.objects.values('student__username').annotate(total_minutes=Sum('duration_minutes')).order_by('-total_minutes')
        return Response(list(qs))
