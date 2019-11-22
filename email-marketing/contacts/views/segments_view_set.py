from rest_framework.viewsets import ModelViewSet

from contacts.models import Segment
from contacts.serializers import SegmentSerializer


class SegmentsViewSet(ModelViewSet):
    serializer_class = SegmentSerializer

    def get_queryset(self):
        return Segment.objects.all()
