import os
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "users": reverse('user-list', request=request, format=format),
        "profiles": reverse('studentprofile-list', request=request, format=format),
        "activities": reverse('activity-list', request=request, format=format),
        "teams": reverse('team-list', request=request, format=format),
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    # explicit API root that returns browsable/host-aware URLs
    path('api/', api_root, name='api-root'),
    # Mount the app API (router will handle /api/<...> endpoints)
    path('api/', include('octofit_tracker.urls')),
    # Redirect site root to the API using a relative URL
    path('', RedirectView.as_view(url='/api/', permanent=False)),
]
