# Generated by Django 4.2.1 on 2023-07-02 14:42

import datetime

from django.db import migrations

from helpers.create_db_objects import create_currency_objects_in_db
from helpers.nbp_api_request import fetch_all_currency_data


def load_currency_data(apps, schema_editor):
    CurrencyName = apps.get_model("currency", "CurrencyName")
    CurrencyDate = apps.get_model("currency", "CurrencyDate")
    CurrencyValue = apps.get_model("currency", "CurrencyValue")

    start_date = datetime.date(2005, 1, 2)
    end_date = datetime.date.today()

    data = fetch_all_currency_data(start_date, end_date)

    create_currency_objects_in_db(data)


def delete_all_currency_data(apps, schema_editor):
    CurrencyName = apps.get_model("currency", "CurrencyName")
    CurrencyDate = apps.get_model("currency", "CurrencyDate")
    CurrencyValue = apps.get_model("currency", "CurrencyValue")

    CurrencyName.objects.all().delete()
    CurrencyDate.objects.all().delete()
    CurrencyValue.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("currency", "0001_initial"),
    ]

    operations = [migrations.RunPython(load_currency_data, delete_all_currency_data)]