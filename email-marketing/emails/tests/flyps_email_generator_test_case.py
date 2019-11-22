from django.test import TestCase
from requests.auth import HTTPBasicAuth

from contacts.models import Contact
from emails.models import EmailTemplate
from emails.utils import FlypsEmailGenerator


class FlypsEmailGeneratorTestCase(TestCase):
    fixtures = ['test_data.json', ]

    def test_getting_data_from_flyps_email_generator(self):
        contact = Contact.objects.get(pk=1)
        template = EmailTemplate.objects.get(pk=1)
        generator = FlypsEmailGenerator(contact, template)
        expected_data = {
            'from': {
                'name': 'Test Header Name',
                'email': 'email_marketing@marketing.com'
            },
            'to': {
                'name': 'John Doe',
                'email': 'test@test.test'
            },
            'subject': 'Hello John!',
            'html': '<html>'
                    '<head></head>'
                    '<body>'
                    'Hi John Doe'
                    '</body>'
                    '</html>',
            'text': 'Hi John Doe',
            'headers': {}
        }
        self.assertEqual(expected_data, generator.get_data())

    def test_getting_auth_from_flyps_email_generator(self):
        contact = Contact.objects.get(pk=1)
        template = EmailTemplate.objects.get(pk=1)
        generator = FlypsEmailGenerator(contact, template)
        self.assertEqual(HTTPBasicAuth('flyps_user', 'flyps_password'), generator.get_auth())
