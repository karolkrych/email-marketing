from django.urls import path

from core.views import ConfigUpdateView


urlpatterns = [
    path('update-config/', ConfigUpdateView.as_view(), name='update-config'),
]
