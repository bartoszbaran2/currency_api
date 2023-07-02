from datetime import datetime

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def test_func():
    logger.info(f"test: {datetime.now()}")
