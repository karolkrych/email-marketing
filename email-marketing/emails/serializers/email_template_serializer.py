from rest_framework.serializers import ModelSerializer

from emails.models import EmailTemplate


class EmailTemplateSerializer(ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = '__all__'
