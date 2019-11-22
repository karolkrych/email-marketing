from rest_framework.serializers import ModelSerializer

from contacts.models import Segment
from contacts.serializers import ContactSerializer


class SegmentSerializer(ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Segment
        fields = '__all__'
