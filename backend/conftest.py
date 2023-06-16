from datetime import date

import pytest

from currency.models import CurrencyDate, CurrencyName, CurrencyValue


@pytest.fixture
def currency_date(db):
    return CurrencyDate.objects.create(date=date(2023, 6, 1))


@pytest.fixture
def currency_date2(db):
    return CurrencyDate.objects.create(date=date(2023, 6, 2))


@pytest.fixture
def currency_name(db):
    return CurrencyName.objects.get(code="USD")


@pytest.fixture
def currency_value(currency_date, currency_name, db):
    return CurrencyValue.objects.create(exchange_rate=0.10, currency_name=currency_name, currency_date=currency_date)


@pytest.fixture
def currency_value2(currency_date2, currency_name, db):
    return CurrencyValue.objects.create(exchange_rate=0.20, currency_name=currency_name, currency_date=currency_date2)
