from django.urls import include, path
from rest_framework.routers import DefaultRouter

from emails.views.email_templates_view_set import EmailTemplatesViewSet
from emails.views.send_emails_api_view import SendEmailsAPIView

router = DefaultRouter()
router.register('email-templates', EmailTemplatesViewSet, basename='email_template')

urlpatterns = [
    path('', include(router.urls)),
    path('send-emails/', SendEmailsAPIView.as_view(), name='send-emails'),
]
