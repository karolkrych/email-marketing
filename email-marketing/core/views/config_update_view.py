from rest_framework.generics import UpdateAPIView

from core.models import Config
from core.serializers import ConfigUpdateSerializer


class ConfigUpdateView(UpdateAPIView):
    serializer_class = ConfigUpdateSerializer

    def get_object(self):
        return Config.load()
