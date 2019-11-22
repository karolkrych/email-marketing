from django.db import models


class EmailTemplate(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    html_content = models.TextField()
    text_content = models.TextField()
