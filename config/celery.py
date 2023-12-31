import os
from celery import Celery
import logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.beat_scheduler = "django_celery_beat.schedulers:DatabaseScheduler"

logger = logging.getLogger('celery')
logger.setLevel(logging.DEBUG)

app.autodiscover_tasks()
