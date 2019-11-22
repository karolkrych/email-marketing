from django.http import HttpResponse
from rest_framework.generics import GenericAPIView

from emails.serializers import SendEmailsSerializer
from emails.tasks import initialize_flyps_email_sender_job_creator


class SendEmailsAPIView(GenericAPIView):
    serializer_class = SendEmailsSerializer

    def post(self, request, format=None):
        """
        Sends email(s) for given contact or contacts segment
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        data = serializer.data
        initialize_flyps_email_sender_job_creator.delay(data.get('template'), data.get('contact'), data.get('segment'))
        return HttpResponse(status=202)
