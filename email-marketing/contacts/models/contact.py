from django.db import models


class Contact(models.Model):
    email_address = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    segment = models.ForeignKey('contacts.Segment', related_name='contacts', on_delete=models.SET_NULL,
                                null=True, blank=True)
