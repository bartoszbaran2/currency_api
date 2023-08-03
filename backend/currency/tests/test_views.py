from django.urls import reverse_lazy


def test_currency_form_view_get(client, multiple_currency_names):
    response = client.get(reverse_lazy("currency:currency_form"))

    assert all(
        (currency.code, currency.name.title()) in response.context["form"].fields["currency"].choices
        for currency in multiple_currency_names
    )


def test_currency_form_view_post_valid(client, currency_values):
    form_data = {
        "start_date": "2023-05-12",
        "end_date": "2023-05-13",
        "currency": ["USD", "CHF", "EUR"],
    }
    response = client.post(reverse_lazy("currency:currency_form"), data=form_data)

    print("*" * 20)
    print("*" * 20)
    print("*" * 20)
    print(currency_values)
    print(response.context["currency_data"])
    print("*" * 20)
    print("*" * 20)
    print("*" * 20)

    assert response.status_code == 200
    assert response.context["currency_data"][0] in currency_values
    assert response.context["currency_data"][1] in currency_values
    assert response.context["currency_data"][2] in currency_values
