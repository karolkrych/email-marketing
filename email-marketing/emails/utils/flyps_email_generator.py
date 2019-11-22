from django.conf import settings
from django.template import Template, Context
from requests.auth import HTTPBasicAuth

from contacts.models import Contact
from core.models import Config
from emails.models import EmailTemplate
from emails.utils import EmailGenerator


class FlypsEmailGenerator(EmailGenerator):

    ENDPOINT_API = settings.FLYPS_ENDPOINT_API

    def __init__(self, recipient: Contact, template: EmailTemplate) -> None:
        self.recipient = recipient
        self.template = template
        self.config = Config.load()

    def _get_rendered_content(self, template: str) -> str:
        t = Template(template)
        return t.render(Context({'recipient': self.recipient}))

    def _get_rendered_text_template(self) -> str:
        return self._get_rendered_content(self.template.text_content)

    def _get_rendered_html_template(self) -> str:
        return self._get_rendered_content(self.template.html_content)

    def _get_sender_data(self) -> dict:
        return {
            'name': self.config.header_name,
            'email': self.config.header_email
        }

    def _get_recipient_data(self) -> dict:
        return {
            'name': f'{self.recipient.first_name} {self.recipient.last_name}',
            'email': self.recipient.email_address
        }

    def _get_rendered_email_subject(self) -> str:
        return self._get_rendered_content(self.template.subject)

    def get_auth(self) -> HTTPBasicAuth:
        return HTTPBasicAuth(self.config.flyps_login, self.config.flyps_password)

    def get_data(self) -> dict:
        return {
            'from': self._get_sender_data(),
            'to': self._get_recipient_data(),
            'subject': self._get_rendered_email_subject(),
            'html': self._get_rendered_html_template(),
            'text': self._get_rendered_text_template(),
            'headers': {}
        }
