from typing import Optional


from contacts.models import Segment, Contact
from emails.models import EmailTemplate


class EmailSenderHandler:
    def __init__(self, template: EmailTemplate, generator_class: type, mail_sending_task,
                 recipient: Optional[Contact] = None, segment: Optional[Segment] = None) -> None:
        """
        :param template: EmailTemplate object with content to send
        :param generator_class: EmailGenerator child object which generates message and subject for given recipient
        :param mail_sending_task: celery task that should be run to send message (we want to send emails asynchronously)
        :param recipient: Contact model instance with recipient data to whom the message is to be sent
        :param segment: Group of Contact instances to whom the message is to be sent
        """
        assert not (recipient is not None and segment is not None), 'You cannot provide both recipient and segment'
        assert not (recipient is None and segment is None), 'You must provide recipient or segment'
        self.template = template
        self.generator_class = generator_class
        self.recipient = recipient
        self.segment = segment
        self.mail_sending_task = mail_sending_task

    def _get_recipients(self) -> list:
        if self.recipient is not None:
            return [self.recipient, ]
        return self.segment.contacts.all()

    def run(self) -> None:
        recipients = self._get_recipients()
        for recipient in recipients:
            self.mail_sending_task.delay(recipient.pk, self.template.pk)
