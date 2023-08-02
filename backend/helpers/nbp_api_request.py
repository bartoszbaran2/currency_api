import datetime
import json
import time
from urllib import request, error


def get_currency_data_from_nbp_api(start_date, end_date):
    url = f"http://api.nbp.pl/api/exchangerates/tables/a/{start_date}/{end_date}"

    with request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    return data


def fetch_all_currency_data(start_date, end_date):
    all_data = []

    while start_date < end_date:
        next_end_date = start_date + datetime.timedelta(days=92)
        if next_end_date > end_date:
            next_end_date = end_date

        data = get_currency_data_from_nbp_api(start_date, next_end_date)
        all_data.extend(data)

        start_date = next_end_date + datetime.timedelta(days=1)

        time.sleep(1)

    return all_data


def get_today_currency_data_from_nbp_api():
    url = f"http://api.nbp.pl/api/exchangerates/tables/a/today/"

    data = None

    try:
        with request.urlopen(url) as response:
            data = json.loads(response.read().decode())
    except error.HTTPError as e:
        data = str(e)

    return data
