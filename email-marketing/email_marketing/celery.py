import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_marketing.settings')

app = Celery('email_marketing')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
