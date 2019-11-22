from rest_framework.serializers import ModelSerializer

from core.models import Config


class ConfigUpdateSerializer(ModelSerializer):
    class Meta:
        model = Config
        exclude = ['id', ]
