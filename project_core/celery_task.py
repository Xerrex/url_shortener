import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_core.settings") 

tasker = Celery("UrlsTasker")
tasker.config_from_object("django.conf:settings", namespace="CELERY")
tasker.autodiscover_tasks()