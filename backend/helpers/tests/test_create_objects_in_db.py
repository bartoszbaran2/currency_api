# from _decimal import Decimal
#
# from currency.models import CurrencyDate
# from helpers.create_db_objects import create_currency_objects_in_db
#
#
# def test_create_objects_in_db(fake_nbp_api_data, db):
#     create_currency_objects_in_db(fake_nbp_api_data)
#
#     created_date = CurrencyDate.objects.get(date="2023-06-09")
#     created_values = created_date.currency_values.all()
#
#     assert created_values[0].exchange_rate == Decimal("4.15450000")
#     assert created_values[0].currency_name.code == "USD"
#     assert created_values[1].exchange_rate == Decimal("4.4717")
#     assert created_values[1].currency_name.code == "EUR"
#     assert created_values[2].exchange_rate == Decimal("5.2106")
#     assert created_values[2].currency_name.code == "GBP"
