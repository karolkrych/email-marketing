from django.db import models


class Segment(models.Model):
    name = models.CharField(max_length=255)
