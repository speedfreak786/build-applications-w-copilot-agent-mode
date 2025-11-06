import os
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.http import JsonResponse
from rest_framework.reverse import reverse


def api_root(request):
    return JsonResponse({
        "users": request.build_absolute_uri(reverse('user-list', request=request)),
        "profiles": request.build_absolute_uri(reverse('studentprofile-list', request=request)),
        "activities": request.build_absolute_uri(reverse('activity-list', request=request)),
        "teams": request.build_absolute_uri(reverse('team-list', request=request)),
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    # explicit API root that returns host-aware absolute URLs
    path('api/', api_root, name='api-root'),
    # Mount the app API (router will handle /api/<...> endpoints)
    path('api/', include('octofit_tracker.urls')),
    # Redirect site root to the API using a relative URL to prevent host-aware redirect loops
    path('', RedirectView.as_view(url='/api/', permanent=False)),
]
