# Generated by Django 4.2.1 on 2023-06-04 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CurrencyDate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField(db_index=True)),
            ],
            options={
                "verbose_name": "Currency Date",
                "verbose_name_plural": "Currency Dates",
            },
        ),
        migrations.CreateModel(
            name="CurrencyName",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=35)),
                ("code", models.CharField(max_length=3)),
            ],
            options={
                "verbose_name": "Currency Name",
                "verbose_name_plural": "Currency Names",
            },
        ),
        migrations.CreateModel(
            name="CurrencyValue",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("exchange_rate", models.DecimalField(decimal_places=8, max_digits=10)),
                (
                    "currency_date",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="currency_values",
                        to="currency.currencydate",
                    ),
                ),
                (
                    "currency_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="currency_values",
                        to="currency.currencyname",
                    ),
                ),
            ],
            options={
                "verbose_name": "Currency Value",
                "verbose_name_plural": "Currency Values",
                "unique_together": {("currency_name", "currency_date")},
            },
        ),
    ]
