from currency.models import CurrencyValue, CurrencyName, CurrencyDate


def create_currency_objects_in_db(data):
    currency_values = [
        CurrencyValue(
            exchange_rate=rate["mid"],
            currency_name=CurrencyName.objects.get_or_create(name=rate["currency"], code=rate["code"])[0],
            currency_date=CurrencyDate.objects.get_or_create(date=table["effectiveDate"])[0],
        )
        for table in data
        for rate in table["rates"]
    ]
    CurrencyValue.objects.bulk_create(currency_values)
