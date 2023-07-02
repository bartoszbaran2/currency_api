from django.shortcuts import render
from django.views.generic import FormView

from . import forms, models


class CurrencyFormView(FormView):
    form_class = forms.CurrencyForm
    template_name = "currency/currency_view.html"
    success_url = "/"

    def get_form(self, form_class=None):
        currencies = models.CurrencyName.objects.all()
        form = super().get_form(form_class)

        form.fields["currency"].choices = [(currency.code, currency.name.title()) for currency in currencies]

        return form
