# from helpers.nbp_api_request import get_currencies_data_from_nbp_api, fetch_all_currency_data
#
#
# def test_currency_data_from_nbp_api_right_request(start_date, end_date):
#     data = get_currencies_data_from_nbp_api(start_date, end_date)
#
#     assert len(data) == 2
#     assert data[0]["effectiveDate"] == "2023-05-23"
#     assert len(data[0]["rates"]) + len(data[1]["rates"]) == 66
#
#
# def test_fetch_all_currency_data_returns_data_from_extended_range(date_above_93_days, end_date):
#     data = fetch_all_currency_data(date_above_93_days, end_date)
#
#     print("*" * 20)
#     print("*" * 20)
#     print("*" * 20)
#     print(data)
#     print("*" * 20)
#     print("*" * 20)
#     print("*" * 20)
#
#     assert len(data) == 65
