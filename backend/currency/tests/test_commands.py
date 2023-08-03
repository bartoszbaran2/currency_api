import sys
import datetime
from io import StringIO
from unittest.mock import patch

from django.core.management import call_command

from currency.models import CurrencyDate


@patch("currency.management.commands.fetch_nbp_data.get_today_currency_data_from_nbp_api")
@patch("currency.management.commands.fetch_nbp_data.create_currency_objects_in_db")
def test_command_handling_no_new_api_data(mock_create_objects_fn, mock_get_data_fn, db):
    mock_get_data_fn.return_value = "HTTP Error 404: Not Found - Brak danych"
    out = StringIO()
    sys.stdout = out

    call_command("fetch_nbp_data")

    mock_create_objects_fn.assert_not_called()
    assert "There are no new data to fetch today" in str(out.getvalue())


@patch("currency.management.commands.fetch_nbp_data.get_today_currency_data_from_nbp_api")
def test_command_handle_new_data_from_api(mock_get_data_fn, fake_nbp_api_data, db):
    mock_get_data_fn.return_value = fake_nbp_api_data
    out = StringIO()
    sys.stdout = out

    call_command("fetch_nbp_data")

    assert "Currency rates successfully fetched and saved to database." in str(out.getvalue())
