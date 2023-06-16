import random
from datetime import date

import pytest
from _decimal import Decimal
from django.db import IntegrityError

from currency.models import CurrencyValue, CurrencyDate, CurrencyName


def test_add_one_currency_data(currency_date, currency_value):
    assert currency_value.currency_name.code == "USD"
    assert currency_value.currency_name.name == "dolar amerykański"
    assert currency_value.currency_date.date == currency_date.date


def test_get_values_by_date_range(currency_value, currency_value2):
    dates = CurrencyDate.objects.filter(date__range=(date(2023, 6, 1), date(2023, 6, 3)))

    values = dates.filter(currency_values__currency_name__code="USD")

    assert len(values) == 2
    assert values.first().currency_values.first().exchange_rate == Decimal("0.1")


def test_add_two_values_for_one_date_and_currency(currency_date, currency_name):
    CurrencyValue.objects.create(exchange_rate=Decimal("1.0"), currency_name=currency_name, currency_date=currency_date)

    with pytest.raises(IntegrityError) as excinfo:
        CurrencyValue.objects.create(
            exchange_rate=Decimal("2.0"), currency_name=currency_name, currency_date=currency_date
        )
    assert "duplicate key value violates unique constraint" in str(excinfo)


def test_add_multiple_exchange_rate_at_once(currency_date):
    currency_names = CurrencyName.objects.all()
    currency_names_count = CurrencyName.objects.all().count()
    values = [Decimal(str(round(random.uniform(0.1, 20), 4))) for _ in range(currency_names_count)]
    currency_values = [
        CurrencyValue(exchange_rate=value, currency_date=currency_date, currency_name=currency_names[index])
        for index, value in enumerate(values)
    ]
    CurrencyValue.objects.bulk_create(currency_values)

    currency_values_db = CurrencyValue.objects.all().count()

    assert currency_values_db == currency_names_count
    assert CurrencyDate.objects.get(date=currency_date.date).currency_values.count() == currency_names_count
    assert currency_names.first().currency_values.filter(currency_date=currency_date).count() == 1
