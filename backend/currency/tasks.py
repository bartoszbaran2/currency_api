from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command

logger = get_task_logger(__name__)


@shared_task
def fetch_nbp_api_task():
    call_command("fetch_nbp_data")
