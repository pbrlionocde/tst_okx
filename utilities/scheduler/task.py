# from celery import Celery

# from main import okx_init

# """
# In oreder to run celery scheduler service you need:
# * celery -A utilities/scheduler/task worker --loglevel=info *
# * celery -A utilities/scheduler/task beat --loglevel=info *
# """

# CLOUD_URL = 'amqps://rnwcnvvv:78nD8njyxFdsOU60KFxG8RGnQ7gz1c-0@sparrow.rmq.cloudamqp.com/rnwcnvvv'
# app = Celery('tasks', broker=CLOUD_URL)


# app.conf.beat_schedule = {
#     'get-info-every-60-seconds': {
#         'task': 'src.scheduler.task.get_info',
#         'schedule': 60.0,
#     },
# }
# app.conf.timezone = 'UTC'


# @app.task
# def get_info():
#     okx_init()
