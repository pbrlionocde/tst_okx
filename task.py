from celery import Celery

from main import okx_balance

"""
In oreder to run celery scheduler service you need:
* celery -A task worker --loglevel=info *
* celery -A task beat --loglevel=info *
"""

CLOUD_URL = 'amqps://nmgjrsmh:cd4OL1QoOp-2i0k56jBelkyGlP-ghWu3@sparrow.rmq.cloudamqp.com/nmgjrsmh'
app = Celery('tasks', broker=CLOUD_URL)


app.conf.beat_schedule = {
    'get-info-every-60-seconds': {
        'task': 'task.get_info',
        'schedule': 60.0,
    },
}
app.conf.timezone = 'UTC'


@app.task
def get_info():
    okx_balance()
