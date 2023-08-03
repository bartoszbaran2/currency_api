import pytest
from django.utils import timezone

from ..forms import CurrencyForm


@pytest.fixture
def currency_choices():
    return [("USD", "dolar amerykański"), ("EUR", "euro")]


def test_currency_form_valid_data(currency_choices):
    form = CurrencyForm(
        data={
            "start_date": "2022-01-01",
            "end_date": "2022-01-10",
            "currency": ["USD", "EUR"],
        }
    )

    form.fields["currency"].choices = currency_choices

    assert form.is_valid()


def test_currency_form_invalid_start_date(currency_choices):
    form = CurrencyForm(
        data={
            "start_date": "2000-01-01",
            "end_date": "2022-01-10",
            "currency": ["USD", "EUR"],
        }
    )

    form.fields["currency"].choices = currency_choices

    assert not form.is_valid()
    assert "Start date cannot be earlier than 2005-01-02." in str(form.errors)


def test_currency_form_invalid_start_date_future(currency_choices):
    future_date = timezone.now().date() + timezone.timedelta(days=1)

    form = CurrencyForm(data={"start_date": str(future_date), "end_date": "2022-01-10", "currency": ["USD", "EUR"]})

    form.fields["currency"].choices = currency_choices

    assert not form.is_valid()
    assert "Start date cannot be in the future." in str(form.errors)


def test_currency_form_invalid_end_date_before_start_date(currency_choices):
    form = CurrencyForm(data={"start_date": "2022-01-10", "end_date": "2022-01-01", "currency": ["USD", "EUR"]})

    form.fields["currency"].choices = currency_choices

    assert not form.is_valid()
    assert "End date cannot be earlier than start date." in str(form.errors)


def test_end_date_not_later_than_today(currency_choices):
    form = CurrencyForm(
        data={"start_date": "2022-01-01", "end_date": timezone.now().date(), "currency": ["USD", "EUR"]}
    )

    form.fields["currency"].choices = currency_choices

    assert not form.is_valid()
    assert "End date must be earlier than today." in str(form.errors)


def test_end_date_not_in_future(currency_choices):
    form = CurrencyForm(
        data={
            "start_date": "2022-01-01",
            "end_date": str(timezone.now().date() + timezone.timedelta(days=1)),
            "currency": ["USD", "EUR"],
        }
    )

    assert not form.is_valid()
    assert "End date cannot be in the future." in str(form.errors)
