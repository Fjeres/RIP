from celery import Celery
import os,sys


sys.path.append(os.path.abspath('backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend', include=['backend.tasks'])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()




# from rabbit.celery import add ress.get(timeout=1)