import datetime

from celery import shared_task
from celery.utils.log import get_task_logger

from currency.models import CurrencyDate
from helpers.create_db_objects import create_currency_objects_in_db
from helpers.nbp_api_request import get_today_currency_data_from_nbp_api

logger = get_task_logger(__name__)


@shared_task
def fetch_nbp_api_task():
    logger.info(f"updating data")
    data = get_today_currency_data_from_nbp_api()

    if data == "HTTP Error 404: Not Found - Brak danych":
        logger.warning(f"There are no new data to fetch {datetime.date.today()}.")
        return

    create_currency_objects_in_db(data)

    created_data_count = CurrencyDate.objects.get(date=data[0]["effectiveDate"]).currency_values.all().count()

    if created_data_count == len(data[0]["rates"]):
        logger.warning(f"Currency rates successfully fetched and saved to database.")
