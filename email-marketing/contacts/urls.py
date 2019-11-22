from django.urls import include, path
from rest_framework.routers import DefaultRouter

from contacts.views import ContactsViewSet
from contacts.views import SegmentsViewSet

router = DefaultRouter()
router.register('contacts', ContactsViewSet, basename='contact')
router.register('segments', SegmentsViewSet, basename='segment')

urlpatterns = [
    path('', include(router.urls)),
]
