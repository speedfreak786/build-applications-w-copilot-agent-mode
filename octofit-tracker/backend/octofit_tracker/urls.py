from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.StudentProfileViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'teams', views.TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
