import os

from celery import Celery



# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rapto_learning.settings')

app = Celery('rapto_learning')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings' , namespace='CELERY')

# app.conf.beat_schedule= {
#     # Executes every Friday at 4pm
#     'send-notification-on-friday-afternoon': { 
#          'task': 'rapto.tasks.send_notification', 
#          'schedule': 10,
#         },          
# }


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')