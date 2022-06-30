from celery.utils.log import get_task_logger
from core.celery import app
from author.models import AuthorModel


logger = get_task_logger(__name__)


@app.task
def add_author():
	AuthorModel.objects.create(name='very_test', desc='very_test')
	return 1

# celery -A core beat
# celery -A core worker -l info
