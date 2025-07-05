import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

# setting the Django settings module.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_project.settings")
app = Celery("todo_project")
app.config_from_object("django.conf:settings", namespace="CELERY")


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Debug task to print request info"""
    print(f"Request: {self.request!r}")
