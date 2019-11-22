from rest_framework.viewsets import ModelViewSet

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactsViewSet(ModelViewSet):
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.all()
