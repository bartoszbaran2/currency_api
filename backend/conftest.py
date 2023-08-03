import datetime
from datetime import date, timedelta

import pytest
from _decimal import Decimal

from currency.models import CurrencyName, CurrencyDate, CurrencyValue


@pytest.fixture
def currency(db, multiple_currency_names):
    currency_name = CurrencyName.objects.get(code="USD")
    currency_date = CurrencyDate.objects.create(date=date(2023, 5, 23))
    currency_value = CurrencyValue.objects.create(
        exchange_rate=1.5, currency_date=currency_date, currency_name=currency_name
    )

    return currency_date


@pytest.fixture
def currency_2(db, multiple_currency_names):
    currency_name = CurrencyName.objects.get(code="USD")
    currency_date = CurrencyDate.objects.create(date=date(2023, 5, 23) - timedelta(days=2))
    currency_value = CurrencyValue.objects.create(
        exchange_rate=15.34, currency_date=currency_date, currency_name=currency_name
    )

    return currency_date


@pytest.fixture
def currency_date(db):
    return CurrencyDate.objects.create(date=date(2023, 5, 12))


@pytest.fixture
def currency_name(db):
    return CurrencyName.objects.create(name="dolar amerykański", code="USD")


@pytest.fixture
def multiple_currency_names(db):
    currency_names = [
        CurrencyName(name="euro", code="EUR"),
        CurrencyName(name="dolar amerykański", code="USD"),
        CurrencyName(name="frank szwajcarski", code="CHF"),
    ]
    CurrencyName.objects.bulk_create(currency_names)

    return currency_names


@pytest.fixture
def start_date():
    return datetime.date(2023, 5, 23)


@pytest.fixture
def end_date():
    return datetime.date(2023, 5, 24)


@pytest.fixture
def date_above_93_days():
    return datetime.date(2023, 5, 24) - datetime.timedelta(days=95)


@pytest.fixture
def currency_values(currency_date, multiple_currency_names):
    for name in multiple_currency_names:
        CurrencyValue.objects.create(exchange_rate=1.5, currency_name=name, currency_date=currency_date)

    values = CurrencyValue.objects.all()

    return values


@pytest.fixture
def fake_nbp_api_data():
    data = [
        {
            "table": "A",
            "no": "110/A/NBP/2023",
            "effectiveDate": "2023-06-09",
            "rates": [
                {"currency": "dolar amerykański", "code": "USD", "mid": 4.1545},
                {"currency": "euro", "code": "EUR", "mid": 4.4717},
                {"currency": "funt szterling", "code": "GBP", "mid": 5.2106},
            ],
        }
    ]
    return data
