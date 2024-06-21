Pre-requisites for installation and working:

install Django and -
pip install django_elasticsearch_dsl

after elasticsearch installation, you will need to add its respective settings in settings.py
and also add elasticsearch to installed apps

'django_elasticsearch_dsl',


##################################################################

install redis and celery for Celery setup
pip install celery redis

update settings for celery and redis:
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379/0") #0 refers to default db
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://redis:6379/0") #0 refers to default db


Elastic Search and Celery are setup using docker-compose file
So, when both are configured properly, elasticsearch automatically assigns tasks to celery.
Following tasks are assigned automatically:

    django_elasticsearch_dsl.signals.registry_delete_task
    django_elasticsearch_dsl.signals.registry_update_related_task
    django_elasticsearch_dsl.signals.registry_update_task
