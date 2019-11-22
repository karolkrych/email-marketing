from django.test import TestCase

from contacts.models import Contact, Segment
from emails.models import EmailTemplate
from emails.tasks import send_with_flyps_to_recipient
from emails.utils import EmailSenderHandler, EmailGenerator


class EmailSenderHandlerTestCase(TestCase):
    fixtures = ['test_data.json', ]

    def test_initializing_email_sender_handler_assertion_error_too_many_args(self):
        contact = Contact.objects.get(pk=1)
        segment = Segment.objects.get(pk=1)
        template = EmailTemplate.objects.get(pk=1)
        args = [template, EmailGenerator, send_with_flyps_to_recipient, contact, segment]
        self.assertRaises(AssertionError, EmailSenderHandler, *args)

    def test_initializing_email_sender_handler_assertion_error_not_enough_args(self):
        template = EmailTemplate.objects.get(pk=1)
        args = [template, EmailGenerator, send_with_flyps_to_recipient]
        self.assertRaises(AssertionError, EmailSenderHandler, *args)

    def test_proper_initializing_email_sender_handler(self):
        contact = Contact.objects.get(pk=1)
        template = EmailTemplate.objects.get(pk=1)
        try:
            EmailSenderHandler(template, EmailGenerator, send_with_flyps_to_recipient, contact)
        except AssertionError:
            self.fail('EmailSenderHandler instance was not initialized')
