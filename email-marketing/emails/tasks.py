from celery import shared_task

from contacts.models import Contact, Segment
from emails.models import EmailTemplate
from emails.utils import FlypsEmailGenerator, EmailSender, EmailSenderHandler


@shared_task
def send_with_flyps_to_recipient(recipient_pk, template_pk):
    recipient = Contact.objects.get(pk=recipient_pk)
    template = EmailTemplate.objects.get(pk=template_pk)
    generator = FlypsEmailGenerator(recipient, template)
    sender = EmailSender(generator)
    sender.send()


@shared_task
def initialize_flyps_email_sender_job_creator(template_pk, recipient_pk=None, segment_pk=None):
    template = EmailTemplate.objects.get(pk=template_pk)
    recipient = Contact.objects.get(pk=recipient_pk) if recipient_pk else None
    segment = Segment.objects.get(pk=segment_pk) if segment_pk else None
    handler = EmailSenderHandler(template, FlypsEmailGenerator, send_with_flyps_to_recipient, recipient, segment)
    handler.run()
