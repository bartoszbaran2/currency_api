from _decimal import Decimal
from datetime import date
import random

import pytest
from django.db import IntegrityError

from ..models import CurrencyName, CurrencyDate, CurrencyValue


def test_add_one_currency_data(currency_name):
    currency_name = CurrencyName.objects.get(code=currency_name.code)
    currency_date = CurrencyDate.objects.create(date=date.today())
    currency_value = CurrencyValue.objects.create(
        exchange_rate=1.5, currency_date=currency_date, currency_name=currency_name
    )

    assert currency_value.currency_name.name == currency_name.name
    assert currency_value.currency_date.date == currency_date.date


def test_get_value_by_date_range(currency, currency_2, multiple_currency_names):
    dates = CurrencyDate.objects.filter(date__range=(date(2023, 5, 20), date(2023, 5, 25)))
    values = dates.filter(currency_values__currency_name__code="USD")

    assert values.count() == 2
    assert values.first().currency_values.first().exchange_rate == Decimal("1.5")


def test_add_two_values_for_one_date_for_one_currency(currency_date, currency_name):
    CurrencyValue.objects.create(
        exchange_rate=Decimal("3.12"), currency_date=currency_date, currency_name=currency_name
    )

    with pytest.raises(IntegrityError) as exc_info:
        CurrencyValue.objects.create(
            exchange_rate=Decimal("4.12"), currency_date=currency_date, currency_name=currency_name
        )

    assert "duplicate key value violates unique constraint" in str(exc_info)


def test_add_multiple_exchange_rate_at_once(currency_date, multiple_currency_names):
    currency_names = CurrencyName.objects.all()
    names_count = currency_names.count()
    values = [Decimal(str(round(random.uniform(2.3, 10.3), 4))) for _ in range(names_count)]
    currency_values = [
        CurrencyValue(exchange_rate=value, currency_date=currency_date, currency_name=currency_names[index])
        for index, value in enumerate(values)
    ]

    CurrencyValue.objects.bulk_create(currency_values)

    saved_values = CurrencyValue.objects.all()

    assert saved_values.count() == names_count
    assert CurrencyDate.objects.get(date=currency_date.date).currency_values.all().count() == names_count
