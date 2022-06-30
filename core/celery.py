from celery import Celery
from core import settings as celeryconfig


app = Celery(
	'core', 
	backend='amqp',
	broker='amqp://guest:guest@localhost:5672/',
)
# app.autodiscover_tasks(packages=['tasks'])

app.config_from_object(celeryconfig)


# @app.on_after_finalize.connect
# def setup_periodic_tasks(sender, **kwargs):
# 	sender.add_periodic_task(3.0, add(1, 2), name='run add task every 3 seconds')


if __name__ == '__main__':
	app.start()

# run celery celery -A core worker -l info
# run rbmq server --> cd /usr/sbin
				# --> sudo rabbitmqctl stop
				# --> sudo rabbitmq-server starts
