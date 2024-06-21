import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery("core") #project folder name
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.conf.task_routes = {'celery_app.tasks.task1': {'queue':'queue1'}, 'celery_app.tasks.task2':{'queue':'queue2'}}
app.autodiscover_tasks() #specifying celery to look for all the tasks