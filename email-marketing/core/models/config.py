from django.db import models


class Config(models.Model):
    flyps_login = models.CharField(max_length=255, null=True, blank=True)
    flyps_password = models.CharField(max_length=255, null=True, blank=True)
    header_email = models.CharField(max_length=255, null=True, blank=True)
    header_name = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Config, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
