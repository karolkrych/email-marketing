from rest_framework.viewsets import ModelViewSet

from emails.models import EmailTemplate
from emails.serializers import EmailTemplateSerializer


class EmailTemplatesViewSet(ModelViewSet):
    serializer_class = EmailTemplateSerializer

    def get_queryset(self):
        return EmailTemplate.objects.all()
