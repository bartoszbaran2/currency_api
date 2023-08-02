import datetime

from django.core.management import BaseCommand

from currency.models import CurrencyDate
from helpers.create_db_objects import create_currency_objects_in_db
from helpers.nbp_api_request import get_today_currency_data_from_nbp_api


class Command(BaseCommand):
    help = "Fetch daily data from NBP API."

    def handle(self, *args, **options):
        data = get_today_currency_data_from_nbp_api()

        if data == "HTTP Error 404: Not Found - Brak danych":
            self.stdout.write(
                self.style.WARNING(
                    f"There are no new data to fetch today. \nDate: {datetime.datetime.today()} \nServer response: {data}"
                )
            )
            return

        create_currency_objects_in_db(data)

        created_data_count = CurrencyDate.objects.get(date=data[0]["effectiveDate"]).currency_values.all().count()

        if created_data_count == len(data[0]["rates"]):
            self.stdout.write(
                self.style.SUCCESS(
                    f"Currency rates successfully fetched and saved to database. \nObjects count: {created_data_count}"
                )
            )
        else:
            self.stdout.write(self.style.WARNING("Currency rates were not created."))
