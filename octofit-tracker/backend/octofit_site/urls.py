import os
from django.contrib import admin
from django.urls import path, include, reverse
from django.views.generic import RedirectView
from django.http import JsonResponse


def api_root(request):
    # Build host-aware absolute URLs without importing DRF at module import time
    return JsonResponse({
        "users": request.build_absolute_uri(reverse('user-list')),
        "profiles": request.build_absolute_uri(reverse('studentprofile-list')),
        "activities": request.build_absolute_uri(reverse('activity-list')),
        "teams": request.build_absolute_uri(reverse('team-list')),
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
